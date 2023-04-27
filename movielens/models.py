from django.db import models


class GenreChoices(models.TextChoices):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    CHILDRENS = "Children's"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    FILM_NOIR = "Film-Noir"
    HORROR = "Horror"
    MUSICAL = "Musical"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCI_FI = "Sci-Fi"
    THRILLER = "Thriller"
    WAR = "War"
    WESTERN = "Western"


class Movie(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    title = models.TextField()

class MovieGenre(models.Model):
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name="genres")
    genre = models.CharField(max_length=32)

class MovieLink(models.Model):
    movie = models.OneToOneField(to=Movie, on_delete=models.CASCADE, related_name="links")
    imdb_id = models.CharField(max_length=255, null=True)
    themoviedb_id = models.CharField(max_length=255, null=True)
