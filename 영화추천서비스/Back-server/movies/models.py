from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.TextField()
    poster_path = models.URLField(max_length=200,null=True)
    vote_average = models.FloatField()

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    score = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


