from django.db.models import ObjectDoesNotExist
from rest_framework import serializers

from movielens.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    def get_genres(self, movie):
        return movie.genres.all().values_list("genre", flat=True)

    def get_links(self, movie):
        try:
            link = movie.links
        except ObjectDoesNotExist:
            return []
        links = []
        if link.imdb_id:
            links.append(f'https://www.imdb.com/title/tt{link.imdb_id}')
        if link.themoviedb_id:
            links.append(f'https://www.themoviedb.org/movie/{link.themoviedb_id}')
        return links

    class Meta:
        model = Movie
        fields = "__all__"
