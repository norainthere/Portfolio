from django.shortcuts import render
from .models import VisualArt, GenerativeArt, Music, MusicProduction, App, StoreItem

def home(request):
    return render(request, 'home.html')

def visual_art(request):
    artworks = VisualArt.objects.all()
    return render(request, 'visual-art.html', {'artworks': artworks})

def generative_art(request):
    artworks = GenerativeArt.objects.all()
    return render(request, 'generative-art.html', {'artworks': artworks})

def music(request):
    tracks = Music.objects.all()
    return render(request, 'music.html', {'tracks': tracks})

def music_production(request):
    tracks = MusicProduction.objects.all()
    return render(request, 'music-production.html', {'tracks': tracks})

def apps(request):
    apps = App.objects.all()
    return render(request, 'apps.html', {'apps': apps})

def store(request):
    items = StoreItem.objects.all()
    return render(request, 'store.html', {'items': items})
