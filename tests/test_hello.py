from django.urls import reverse
import pytest
from rest_framework import status

pytestmark = [pytest.mark.django_db, pytest.mark.api]

def assert_response_json(response, expected_json, status_code=None):
    __tracebackhide__ = True
    status_code = status_code or status.HTTP_200_OK
    assert response.status_code == status_code
    assert response.json() == expected_json

def test_movies_list(client):
    url = reverse("movies-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
