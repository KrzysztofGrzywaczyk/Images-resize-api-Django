from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import ImageFactory, LinkFactory
import pytest


register(ImageFactory)
register(LinkFactory)

@pytest.fixture
def api_client():
    return APIClient