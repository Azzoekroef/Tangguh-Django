from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=254,blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    point = models.IntegerField(default=0)
    nik = models.IntegerField(blank=True, null=True)
    is_hiden = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.username



