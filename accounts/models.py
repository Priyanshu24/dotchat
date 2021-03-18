from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        _('email address'),
        unique=True
    )
    
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        _('first name'),
        max_length=30,
        unique=False,
        blank=False,
        null=False
    )

    last_name = models.CharField(
        _('last name'),
        max_length=30,
        unique=False,
        blank=False,
        null=False
    )

    is_staff = models.BooleanField(
        default=False
    )
    
    is_active = models.BooleanField(
        default=True
    )
    
    date_joined = models.DateTimeField(
        default=timezone.now
    )

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name'
    ]

    objects = UserManager()

    def __str__(self):
        return self.email