from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if getattr(settings, "DEBUG", False):
   urlpatterns += [path('', include('develop.urls'))]
