from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200)

    def __str__(self):
        return self.movie_title

    # check if the title is englis
    def was_english_title(self):
        return self.movie_title.replace(" ","").isalpha()

class Movie_data(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_data_genre = models.CharField(max_length=200)

    def __str__(self):
        return self.movie_data_genre
