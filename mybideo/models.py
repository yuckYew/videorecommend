from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.movie_title

    # check if the title is englis
    def was_english_title(self):
        return self.movie_title.replace(" ","").isalpha()

class MovieGenre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class MovieInfo(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # TODO: create individual table for movie genre
    movie_genre = models.ForeignKey(MovieGenre, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.movie_title
