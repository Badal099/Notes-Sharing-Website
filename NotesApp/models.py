from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    branch = models.CharField(max_length=40)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username


        
        