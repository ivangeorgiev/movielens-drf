from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from apis.filters import MovieFilter
from apis.serializers import MovieSerializer
from movielens.models import Movie


class RootView(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "movies": reverse("movies-list", request=request),
            }
        )


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_class = MovieFilter
