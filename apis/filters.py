import django_filters

from movielens.models import Movie


class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            "title": ["exact", "contains"],
        }
