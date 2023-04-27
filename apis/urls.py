from django.urls import path, include
from rest_framework import routers
from .views import RootView, MovieViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet, 'movies')

urlpatterns = [
    path('', RootView.as_view(), name="api-root"),
    path('', include(router.urls)),
]
