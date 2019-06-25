# Django
from django.contrib.auth.models import BaseUserManager


class AuthUserManager(BaseUserManager):

    """Manager for BaseNxUser model"""

    def get_queryset(self):
        return super(AuthUserManager, self).get_queryset().filter(
            is_active=True)

    def create_user(self, user, password, **kwargs):
        user = self.model(email=user, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user, password):
        user = self.create_user(user=user, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user
