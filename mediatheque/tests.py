from django.test import TestCase
from django.core.exceptions import ValidationError
from bibliothecaire.models import Membre, Media, Emprunt
from datetime import date, timedelta
from django.utils import timezone

class MembreModelTest(TestCase):

    def setUp(self):
        self.membre = Membre.objects.create(nom="Doe", prenom="John", phone="0746764646", email="john.doe@example.com")

    def test_membre_creation(self):
        self.assertEqual(self.membre.nom, "Doe")
        self.assertEqual(self.membre.prenom, "John")
        self.assertEqual(self.membre.phone, "0746764646")
        self.assertEqual(self.membre.email, "john.doe@example.com")

class MediaModelTest(TestCase):

    def setUp(self):
        self.media = Media.objects.create(titre="Test Livre", auteur_realisateur_artiste="Auteur Test", type_media="livre")

    def test_media_creation(self):
        self.assertEqual(self.media.titre, "Test Livre")
        self.assertEqual(self.media.auteur_realisateur_artiste, "Auteur Test")
        self.assertEqual(self.media.type_media, "livre")


class EmpruntModelTest(TestCase):

    def setUp(self):
        self.membre = Membre.objects.create(nom="Doe", prenom="John", phone="0746764646", email="john.doe@example.com")
        self.media = Media.objects.create(titre="Test Livre", auteur_realisateur_artiste="Auteur Test", type_media="livre")
        self.emprunt = Emprunt.objects.create(media=self.media, emprunteur=self.membre)

    def test_emprunt_creation(self):
        self.assertEqual(self.emprunt.media, self.media)
        self.assertEqual(self.emprunt.emprunteur, self.membre)
        self.assertEqual(self.emprunt.date_emprunt, date.today())
        self.assertEqual(self.emprunt.date_retour, date.today() + timedelta(days=7))

    def test_emprunt_validation(self):
        # Test pour plus de 3 emprunts
        for _ in range(3):
            Emprunt.objects.create(media=self.media, emprunteur=self.membre, date_retour=date.today() + timedelta(days=7))
        new_emprunt = Emprunt(media=self.media, emprunteur=self.membre, date_retour=date.today() + timedelta(days=7))
        with self.assertRaises(ValidationError):
            new_emprunt.clean()

        # Test pour les jeux de plateau
        jeu = Media.objects.create(titre="Test Jeu", auteur_realisateur_artiste="Auteur Test", type_media="jeu")
        new_emprunt = Emprunt(media=jeu, emprunteur=self.membre, date_retour=date.today() + timedelta(days=7))
        with self.assertRaises(ValidationError):
            new_emprunt.clean()

        # Test pour les emprunts en retard
        emprunt_retard = Emprunt.objects.create(media=self.media, emprunteur=self.membre, date_emprunt=timezone.now() - timedelta(days=8), date_retour=None)
        new_emprunt = Emprunt(media=self.media, emprunteur=self.membre, date_retour=date.today() + timedelta(days=7))
        with self.assertRaises(ValidationError):
            new_emprunt.clean()



