from django.db import models
from django import forms

# Create your models here.
from pickle import TRUE
from django.db import models

class RegisterUsers(models.Model):
    user = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    
    class Meta:
        db_table = 'register'