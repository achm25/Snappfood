from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=200,)
    Address = models.CharField(max_length=100)
    District = models.CharField(max_length=50)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.IntegerField(default=1000000,blank=True)