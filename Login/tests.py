from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CreateStudentForm

# Create your tests here.


class LoginUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_successful(self):
        response = self.client.post(self.login_url, {'Email': 'testuser', 'Password': 'testpassword'})
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, 'Login Sucessful')

    def test_login_failed(self):
        response = self.client.post(self.login_url, {'Email': 'testuser', 'Password': 'wrongpassword'})
        self.assertRedirects(response, self.login_url)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, 'There Was An Error Logging In, Please Try Again')

    def test_get_request(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')

class LogoutUserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_logout_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the logout_user view
        response = self.client.get(reverse('logout'))

        # Check that the user is redirected to the home page
        self.assertRedirects(response, reverse('home'))

        # Check that the user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)

        # Check that the success message is displayed
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You Were Logged Out')


class StudentRegisterTest(TestCase):
    def setUp(self):
        self.url = reverse('student_register')
        self.valid_data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'Security_Question1_Answer': 'Answer1',
            'Security_Question2_Answer': 'Answer2',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '1234567890',
            'Net_ID': '123456',
            'password1': 'testpassword',
            'password2': 'testpassword',
            # Add other required fields here
        }
        self.invalid_data = {
            # Add invalid data here
            'email': 'testexample.com',
            'username': 'testuser',
            'Security_Question1_Answer': 'Answer1',
            'Security_Question2_Answer': 'Answer2',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'phone_number': '1234567890',
            'Net_ID': '123456',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

    def test_student_register_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/student_register.html')

    def test_student_register_view_post_valid_data(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Redirects to home page
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(email=self.valid_data['email']).exists())

    def test_student_register_view_post_invalid_data(self):
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/student_register.html')
        self.assertFormError(response, 'form', field='email', errors='This field is required')
        # Add more form validation checks here


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')  # Replace 'register' with the actual URL name

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/scholarship_administrator_register.html')

    def test_register_view_post_valid_data(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            # Add other required form fields here
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertRedirects(response, reverse('home'))  # Replace 'home' with the actual URL name
        # Add additional assertions to check if the user is created and logged in

    def test_register_view_post_invalid_data(self):
        data = {
            'email': 'invalid_email',
            'password': 'short',
            # Add other invalid form fields here
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/scholarship_administrator_register.html')
        # Add additional assertions to check if the form errors are displayed correctly