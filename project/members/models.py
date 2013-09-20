from django.db import models
from django.contrib.auth.models import User
from custom_user.models import AbstractEmailUser

class MyCustomEmailUser(AbstractEmailUser):
  paid = models.BooleanField()
  phone = models.CharField(max_length=15,blank=True)
  street = models.CharField(max_length=100,blank=True)
  city = models.CharField(max_length=100,blank=True)
  state = models.CharField(max_length=2,blank=True)
  zip_code = models.CharField(max_length=15,blank=True)



