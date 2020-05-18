from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """ Test creating new user with email successfull """
        email = "hnarayanan@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(

            email=email,
            password=password
        )



        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for new user is normalized """
        email = "test@HARICUDANT.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email address """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')