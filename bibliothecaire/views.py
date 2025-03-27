# bibliothecaire/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Membre, Media, Emprunt
from .forms import MembreForm, MediaForm, EmpruntForm
from django.utils import timezone
from datetime import datetime, timedelta

def creer_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'bibliothecaire/creer_membre.html', {'form': form})

def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliothecaire/liste_membres.html', {'membres': membres})

def mettre_a_jour_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'bibliothecaire/mettre_a_jour_membre.html', {'form': form})

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, 'bibliothecaire/liste_medias.html', {'medias': medias})

def creer_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_emprunts')
    else:
        form = EmpruntForm()
    return render(request, 'bibliothecaire/creer_emprunt.html', {'form': form})

def ajouter_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')
    else:
        form = MediaForm()
    return render(request, 'bibliothecaire/ajouter_media.html', {'form': form})

def rentrer_emprunt(request, pk):
    emprunt = get_object_or_404(Emprunt, pk=pk)
    emprunt.date_retour = timezone.now()
    emprunt.save()
    return redirect('liste_emprunts')

from django.shortcuts import render
from .models import Media, Membre, Emprunt

def accueil(request):
    return render(request, 'accueil.html')

def media_list(request):
    medias = Media.objects.all()
    return render(request, 'liste_medias.html', {'medias': medias})

def membre_list(request):
    membres = Membre.objects.all()
    return render(request, 'liste_membres.html', {'membres': membres})

def emprunt_list(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'liste_emprunt.html', {'emprunts': emprunts})

def create_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'create_membre.html', {'form': form})

def create_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_medias')  
    else:
        form = MediaForm()
    return render(request, 'create_media.html', {'form': form})

def modifier_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'modifier_membre.html', {'form': form})
