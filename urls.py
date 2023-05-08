from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visual-art/', views.visual_art, name='visual_art'),
    path('generative-art/', views.generative_art, name='generative_art'),
    path('music/', views.music, name='music'),
    path('music-production/', views.music_production, name='music_production'),
    path('apps/', views.apps, name='apps'),
    path('store/', views.store, name='store'),
]
