import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have email.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER = 'CU'
    USER_TYPE = [
        ('AD', 'Admin'),
        ('DR', 'Driver'),
        (CUSTOMER, 'Customer')
    ]

    email         = models.EmailField(unique=True)
    password      = models.CharField(max_length=255)
    first_name    = models.CharField(max_length=255, blank=True)
    last_name     = models.CharField(max_length=255, blank=True)
    phone         = models.CharField(max_length=255, blank=True)
    zipcode       = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    type          = models.CharField(max_length=255, choices=USER_TYPE, default=CUSTOMER)

    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return (self.first_name + ' ' +  self.last_name)

    def get_short_name(self):
        return self.email

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        payload = {
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }
        token = jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')

        # return token.decode('utf-8')
        return token
