from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from .views import profile
from django.urls import reverse
from django.test import Client


# Testing User Creation and then test if his profile works fine
class ProfileTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@gmail.com', password='prova1234')

    def test_details(self):
        request = self.factory.get('/profile')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)


class HomePageTest(TestCase):

    def testHome(self):
        client = Client()
        response = client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
