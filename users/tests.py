from django.test import TestCase
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from .views import profile

# Testing User Creation and then test if his profile works fine
class ProfileTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@gmail.com', password='prova1234')

    def test_details(self):
        request = self.factory.get('/profile')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test my_view() as if it were deployed at /customer/details
        response = profile(request)
        # Use this syntax for class-based views.
        self.assertEqual(response.status_code, 200)