from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Movie

# Create your views here.
def index(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list}
    return render(request, 'mybideo/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'mybideo/detail.html', {'movie': movie})
