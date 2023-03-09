import pytest
# from django.conf import settings
from django.contrib.auth.models import User


pytestmark = pytest.mark.django_db

# User = settings.AUTH_USER_MODEL

class TestImageModel:
    def test_string_output(self,image_factory):
        self.user = User.objects.create_user(username='testuser', password='12345')
        # login = self.client.login(username='testuser', password='12345')
        x = image_factory(name='test_name')
        assert x.__str__() == "Image: test_name"

class TestLinkModel:
    def test_string_output(self,link_factory):
        self.user = User.objects.create_user(username='testuser', password='12345')
        # login = self.client.login(username='testuser', password='12345')
        x = link_factory()
        assert x.__str__() == "testuser's link"
