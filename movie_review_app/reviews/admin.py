from django.contrib import admin

from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'genre')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)



# Register your models here.


