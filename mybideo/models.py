from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.movie_title

    # check if the title is english
    def was_english_title(self):
        return self.movie_title.replace(" ","").isalpha()

class MovieGenre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class MovieDirector(models.Model):
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.director

class MovieCast(models.Model):
    cast = models.CharField(max_length=50)

    def __str__(self):
        return self.cast

class MovieInfo(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    movie_genre = models.ForeignKey(
        MovieGenre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    movie_director = models.OneToOneField(
        MovieDirector,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    movie_cast = models.ForeignKey(
        MovieCast,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.movie.movie_title
