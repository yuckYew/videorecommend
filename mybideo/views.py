import numpy as np
import random

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Movie, MovieInfo

# Create your views here.
"""
def index(request):
    movie_all = np.array(Movie.objects.all())
    choice_index = random.sample(range(1, len(movie_all)), 3)
    movie_list = list(movie_list[choice_index])
    context = {'movie_list', movie_list}
    return render(request, 'mybideo/index.html', context)
"""
class IndexView(generic.ListView):
    template_name = 'mybideo/index.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        """Return list of movies"""
        # return Movie.objects.all()[0:3]
        return list(np.random.choice(Movie.objects.all(), size=3, replace=False))

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'mybideo/detail.html'
