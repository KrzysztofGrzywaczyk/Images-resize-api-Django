from django.test import TestCase
from django.contrib.auth.models import User

class URLTests(TestCase):
    def test_all_imgs(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/api/images')
        self.assertEqual(response.status_code, 200)


