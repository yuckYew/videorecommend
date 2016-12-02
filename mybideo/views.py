from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Movie, Movie_data

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'mybideo/index.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        """Return list of movies"""
        return Movie.objects.all()

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'mybideo/detail.html'
