from django.db import models
from django.conf import settings

class Movie(models.Model):

    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, 
        on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} review'.format(self.movie.title)

class Vote(models.Model):
    reviews = models.ManyToManyField(Review, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)