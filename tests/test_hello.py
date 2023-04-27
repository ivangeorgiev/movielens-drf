from django.urls import reverse
from rest_framework import status

def assert_response_json(response, expected_json, status_code=None):
    __tracebackhide__ = True
    status_code = status_code or status.HTTP_200_OK
    assert response.status_code == status_code
    assert response.json() == expected_json


def test_hello(client):
    url = reverse("hello-world")
    response = client.get(url)
    assert_response_json(response, "Hello, World!")
