from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from django.utils import timezone

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default='DefaultPrenom')
    phone = models.CharField(max_length=10, default='0746764646')
    email = models.EmailField(default='example@example.com')
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Media(models.Model):
    TYPE_CHOICES = [
        ('livre', 'Livre'),
        ('dvd', 'DVD'),
        ('cd', 'CD'),
        ('jeu', 'Jeu de Plateau'),
    ]
    titre = models.CharField(max_length=100)
    auteur_realisateur_artiste = models.CharField(max_length=100)
    type_media = models.CharField(max_length=10, choices=TYPE_CHOICES)
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media_images/', blank=True, null=True)
    description = models.TextField(max_length=2000, null=True, default="", blank=True)

    def __str__(self):
        return f"{self.titre}"

class Emprunt(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(Membre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(default=date.today, null=False)
    date_retour = models.DateField(default=date.today() + timezone.timedelta(days=7))
    returner = models.BooleanField(default=False)

    def clean(self):
        if self.emprunteur.emprunt_set.filter(date_retour__isnull=True).count() >= 3:
            raise ValidationError('Un membre ne peut pas avoir plus de 3 emprunts à la fois.')
        if self.media.type_media == 'jeu':
            raise ValidationError('Les jeux de plateaux ne peuvent pas être empruntés.')
        if self.emprunteur.emprunt_set.filter(date_retour__isnull=True, date_emprunt__lt=timezone.now() - timedelta(days=7)).exists():
            raise ValidationError('Un membre ayant un emprunt en retard ne peut plus emprunter.')

    def __str__(self):
        return f"{self.media} emprunté par {self.emprunteur}"