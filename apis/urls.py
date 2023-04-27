from django.urls import path, include
from rest_framework import routers
from .views import RootView, HelloWorldView

router = routers.DefaultRouter()
# router.register(r'master', MasterViewSet)

urlpatterns = [
    path('', RootView.as_view(), name="api-root"),
    path('hello/', HelloWorldView.as_view(), name="hello-world"),
    # path('', include(router.urls)),
]