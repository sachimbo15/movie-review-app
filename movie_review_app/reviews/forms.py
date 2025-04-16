from django import forms
from .models import Review, MovieSuggestion

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']


class MovieSuggestionForm(forms.ModelForm):
    class Meta:
        model = MovieSuggestion
        fields = '__all__'