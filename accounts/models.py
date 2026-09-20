from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

# Create your models here.



class User(AbstractBaseUser,PermissionsMixin):
    phone=models.CharField(max_length=11,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'phone'
    objects=UserManager()



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    no_show_count=models.IntegerField(default=0)
    suspended_until=models.DateTimeField(null=True,blank=True)
