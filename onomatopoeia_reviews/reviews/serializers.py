from rest_framework import serializers
from reviews.models import Movie



class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'director']