from django.test import TestCase
# from django.test.client import Client
# from django.conf import settings

from .models import User


class LoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="test@example.com",
            password="password"
        )

    def login_test(self):
        self.assertEqual(self.user.username, "test")
