from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        pass

    def create_superuser(self, phone, password, **extra_fields):
        pass