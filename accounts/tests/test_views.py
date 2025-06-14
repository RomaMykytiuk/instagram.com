from django.test import TestCase
from django.urls import reverse

from accounts.forms import UserRegistrationForm,LoginForm
from accounts.models import User

class AccountsViewsTest(TestCase):
    def setUp(self):
        self.register_url = reverse('accounts:register')
        self.login_url = reverse('accounts:login')
        self.logout_url = reverse('accounts:logout')

        self.user = User.objects.create_user(
            username='testuser',
            full_name='Test User',
            password='testpassword123',
            email='testuser@example.com'
        )

    def test_register_success(self):
        response = self.client.post(self.register_url,{
            'username':'newuser',
            'password':'testpassword123',
            'confirm_password': 'testpassword123',
            'email':'testuser@example.com'
        })
        self.assertEqual(response.status_code, 302)
#        self.assertRedirects(response, self.home_url)
        self.assertTrue(User.objects.filter(username='newuser').exists())


