from django.test import TestCase, Client
from django.urls import reverse
from .models import User


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        url = reverse('accounts:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            phone_number='08000000000',
            password='L8W4,W%3PC3P'
        )

    def test_signup_view(self):
        url = reverse('accounts:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'phone_number': "08012345678",
            'password1': 'L8W4,W%3PC3P',
            'password2': 'L8W4,W%3PC3P'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:index'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        url = reverse('accounts:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        data = {
            'username': 'testuser',
            'password': 'L8W4,W%3PC3P'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        self.client.login(username='testuser', password='L8W4,W%3PC3P')
        url = reverse('accounts:logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:login'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
