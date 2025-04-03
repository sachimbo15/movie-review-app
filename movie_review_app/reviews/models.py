from django.db import models

class Movie(models.Models):
    title = models.CharField(max_length=255)
    release_year = models.ImageField()
    genre = models.CharField(max_length=100)

class Review(models.Models):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title