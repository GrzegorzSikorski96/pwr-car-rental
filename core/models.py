from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.full_clean()
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address = models.ForeignKey(
        'core.Address',
        on_delete=models.DO_NOTHING,
        related_name='users',
    )
    contacts = models.ManyToManyField(
        'core.Contact',
        related_name='users',
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()


class Address(models.Model):
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=15)
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=150)


class Contact(models.Model):
    EMAIL = 'e-mail'
    PHONE_NUMBER = 'phone number'

    CONTACT_FORMS_CHOICES = [
        (EMAIL, 'Email'),
        (PHONE_NUMBER, 'Phone number'),
    ]

    value = models.CharField(max_length=150)
    type = models.CharField(max_length=20, choices=CONTACT_FORMS_CHOICES)
