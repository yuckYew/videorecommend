from django.contrib import admin

# Register your models here.
from .models import Movie, MovieInfo, MovieGenre, MovieDirector

class MovieInfoInline(admin.TabularInline):
    model = MovieInfo
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['movie_title']}),
        ('Image path',      {'fields': ['image_path']}),
    ]
    inlines = [MovieInfoInline]

admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieGenre)
admin.site.register(MovieDirector)
