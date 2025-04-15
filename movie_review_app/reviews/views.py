from django.shortcuts import render, redirect
from .models import Movie
from .forms import ReviewForm

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




# Create your views here.
