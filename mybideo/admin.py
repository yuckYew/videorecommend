from django.contrib import admin

# Register your models here.
from .models import Movie, Movie_data

class Movie_dataInline(admin.StackedInline):
    model = Movie_data
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['movie_title']}),
        ('Image path',      {'fields': ['image_path']}),
    ]
    inlines = [Movie_dataInline]
admin.site.register(Movie, MovieAdmin)
