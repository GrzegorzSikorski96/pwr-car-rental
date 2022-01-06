from django.test import TestCase

from core.tests.helpers.sample_objects import sample_user
from django.core.exceptions import ValidationError


class UserModelTestCase(TestCase):
    def test_create_user_with_email_successful(self) -> None:
        email = 'username@example.com'
        password = 'password'
        user = sample_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalized_email(self) -> None:
        email = 'username@EXAMPLE.com'
        user = sample_user(email=email)

        self.assertEqual(user.email, email.lower())

    def test_create_user_with_invalid_email(self) -> None:
        with self.assertRaises(ValidationError):
            sample_user(email='username.example.com')

    def test_create_user_with_invalid_email_2(self) -> None:
        with self.assertRaises(ValidationError):
            sample_user(email='username@com')

    def test_create_user_with_invalid_email_fails_none(self):
        with self.assertRaises(ValidationError):
            sample_user(email=None)

    def test_create_user_with_invalid_email_fails_empty(self):
        with self.assertRaises(ValidationError):
            sample_user(email='')

    def test_create_user_with_invalid_email_fails_spaces(self):
        with self.assertRaises(ValidationError):
            sample_user(email='   ')

    def test_create_user_without_address(self):
        with self.assertRaises(ValidationError):
            sample_user(address_id=None)
