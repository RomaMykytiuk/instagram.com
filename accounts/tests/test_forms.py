from django.test import TestCase

from accounts.forms import UserRegistrationForm
from accounts.models import User

class UserRegistrationFormTests(TestCase):
    def test_valid_form(self):
        form = UserRegistrationForm(data={
            'username':'testuser',
            'email':'test@gmail.com',
            'password':'0604',
            'confirm_password':'0604',
        })
        self.assertTrue(form.is_valid())
    def test_invalid_when_email_empty(self):
        form = UserRegistrationForm(data={
            'username': 'testuser1',
            'email': '',
            'password': '1234',
            'confirm_password': '1234',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email',form.errors)


    def test_invalid_when_username_empty(self):
        form = UserRegistrationForm(data={
            'username': '',
            'email': 'test1@gmail.com',
            'password': '1234',
            'confirm_password': '1234',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
    def test_duplicate_username(self):
        User.objects.create_user(
            username='test42',
            email='test42@gmail.com',
            password='42',
        )
        form = UserRegistrationForm(data={
            'username': 'test42',
            'email': 'test@gmail.com',
            'password': '0604',
            'confirm_password': '0604',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


    def test_invalid_when_passwords_dont_match(self):
        form = UserRegistrationForm(data={
            'username': 'test2',
            'email': 'test1@gmail.com',
            'password': '1234',
            'confirm_password': '7654',
        })
        self.assertFalse(form.is_valid())



