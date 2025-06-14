from django.test import TestCase

from accounts.forms import UserRegistrationForm,LoginForm
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


    def test_duplicate_email(self):
        User.objects.create_user(
            username='test4',
            email='test0@gmail.com',
            password='0604',
        )
        form = UserRegistrationForm(data={
            'username': 'test0',
            'email': 'test0@gmail.com',
            'password': '0604',
            'confirm_password': '0604',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

class UserLoginFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='0604',
        )

    def test_login_with_username(self):
        form = LoginForm(data={
            'login': 'test',
            'password': '0604',
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.user,self.user)

    def test_login_with_email(self):
        form = LoginForm(data={
            'login': 'test@gmail.com',
            'password': '0604',
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.user, self.user)

    def test_invalid_username(self):
        form = LoginForm(data={
            'login': 'test1',
            'password': '0604',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__',form.errors)
        self.assertEqual(form.errors['__all__'][0],'невірний username/email  або пароль')

    def test_invalid_email(self):
        form = LoginForm(data={
            'login': 'test42@gmail.com',
            'password': '0604'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'][0], 'невірний username/email  або пароль')

    def test_invalid_password(self):
        form = LoginForm(data={
            'login':'test',
            'password':'0000'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'][0], 'невірний username/email  або пароль')