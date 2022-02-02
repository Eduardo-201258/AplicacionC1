from pickle import TRUE
from django.db import models

class RegisterUsers(models.Model):
    user = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = 'register'