from django.shortcuts import render, redirect
from .models import Movie, MovieSuggestion
from .forms import ReviewForm, MovieSuggestionForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "reviews/movie_list.html", {"movies": movies})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = ReviewForm()

    return render(request, "reviews/add_review.html", {"form": form})


def suggest_movie(request):
    if request.method == 'POST':
        form = MovieSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suggested_page')
    else:
        form = MovieSuggestionForm()

    return render(request, "reviews/suggest_movie.html", {"form": form})


def suggested_page(request):
    return render(request, "reviews/suggested_page.html")
# Create your views here.
