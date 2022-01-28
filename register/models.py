from django.utils import timezone
from pickle import TRUE
from django.db import models

class RegisterUsers(models.Model):
    usuario = models.CharField(max_length=255, null=True)
    correo = models.IntegerField(null = True, default=0)
    contraseña = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'register_users'
