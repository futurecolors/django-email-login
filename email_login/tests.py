# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class TestEmailAuthenticationFormClean(TestCase):

    def test_empty(self):
        response = self.client.post(reverse('auth_login'), data={})
        self.assertFormError(response, 'form', 'email', [u'This field is required.'])
        self.assertFormError(response, 'form', 'password', [u'This field is required.'])

    def test_wrong_email(self):
        response = self.client.post(reverse('auth_login'), data={'email': '1@1.ru', 'password': 'pass'})
        self.assertFormError(response, 'form', None, [u'Please enter a correct email address and password.'])

    def test_success(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        response = self.client.post(reverse('auth_login'), data={'email': 'lennon@thebeatles.com',
                                                                 'password': 'johnpassword'})
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL)
