from django.db import models

class VisualArt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='visual-art/')

class GenerativeArt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='generative-art/')

class Music(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    soundcloud_link = models.URLField(blank=True)
    bandcamp_link = models.URLField(blank=True)

class MusicProduction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    soundcloud_link = models.URLField(blank=True)

class App(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    app_link = models.URLField()

class StoreItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='store/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
