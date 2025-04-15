from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)

class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class MovieSuggestion(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1899), MaxValueValidator(2100)])
    why_suggested = models.TextField()
    suggestion_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title