import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Указанное имя пользователя должно быть установлено')

        if not email:
            raise ValueError('Данный адрес электронной почты должен быть установлен')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


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
    username      = models.CharField(max_length=255, blank=True, unique=True)

    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'username']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей,
        как обработка электронной почты.
        Обычно это имя и фамилия пользователя.
        Поскольку мы не храним настоящее имя пользователя,
        мы возвращаем его имя пользователя.
        """
        return (self.first_name + ' ' +  self.last_name)

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        payload = {
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }
        token = jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')

        # return token.decode('utf-8')
        return token
