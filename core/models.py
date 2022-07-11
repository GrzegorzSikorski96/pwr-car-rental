from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import QuerySet
from django.utils.text import slugify

from core.checkers.user_checkers import has_group
from core.models_mixins.TimeStampMixin import TimeStampMixin


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
    phone_number = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        permissions = [
            ('employee_views', 'Can enter employee views'),
            ('client_views', 'Can enter client views'),
        ]

    def delete(self, **kwargs):
        if 0 < self.rents.all().count():
            for rent in self.rents.all():
                rent.delete()

        super(User, self).delete()

    def __str__(self):
        return "#%d - %s %s" % (self.pk, self.first_name, self.last_name)


class RestrictedAddressManager(models.Manager):
    def get_query(self, user) -> 'QuerySet[Address]':
        if user:
            if has_group(user, 'employee'):
                return self.all()
            else:
                return self.filter(rent__rented_by=user)

        return self.none()


class Address(TimeStampMixin):
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=15)
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    user = models.ForeignKey('core.User', null=True, on_delete=models.CASCADE, related_name='addresses')
    is_service = models.BooleanField(default=False)
    is_depot = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s %s, %s %s' % (self.country, self.city, self.postal_code, self.street, self.number)

    def get_slugged_address(self):
        return slugify(self.__str__())

    def save(self, *args, **kwargs) -> None:
        super(Address, self).save(*args, **kwargs)
