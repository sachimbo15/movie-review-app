from django.db import models

class Movie(models.Models):
    title = models.CharField(max_length=255)
    release_year = models.ImageField()
    genre = models.CharField(max_length=100)