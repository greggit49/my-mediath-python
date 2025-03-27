# bibliothecaire/forms.py
from django import forms
from .models import Membre, Media, Emprunt

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom','prenom','phone', 'email', 'bloque']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['titre', 'auteur_realisateur_artiste', 'type_media', 'disponible','image', 'description']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['media', 'emprunteur','date_emprunt', 'date_retour', 'returner']