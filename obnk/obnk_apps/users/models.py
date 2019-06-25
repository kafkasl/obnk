# Django
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# obnk
from managers import AuthUserManager

# Python
from uuid import uuid4


class User(PermissionsMixin, AbstractBaseUser):

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    # User data
    uuid = models.UUIDField(primary_key=True, default=uuid4,
                            editable=False)
    email = models.EmailField('email address', unique=True)

    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)

    account_balance = models.FloatField(default=0)
    # Managers
    objects = AuthUserManager()

    # Required for AbstractBaseUser
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email
