from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class RootView(APIView):
    def get(self, request, format=None):
        return Response({
            "hello": reverse("hello-world", request=request),
        })

class HelloWorldView(APIView):
    def get(self, request, format=None):
        return Response("Hello, World!")
