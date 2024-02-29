from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CreateStudentForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Create your tests here.


class UserModelTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        email = "test@example.com"
        username = "testuser"
        password = "testpassword"
        user = User.objects.create_user(email=email, username=username, password=password)
        
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))


    def test_create_bad_user(self):
        User = get_user_model()
        email = "testexample.com"
        username = "testuser"
        password = "testpassword"
        try:
            user = User.objects.create_user(email=email, username=username, password=password)
            user.full_clean()  # This will validate the email field
        except ValidationError:
            user = None

        self.assertEqual(user, None)

