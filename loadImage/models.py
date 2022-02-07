from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
from django.db import models
from django.utils import timezone

class ImgModel(models.Model):
    name_img = models.CharField(max_length=255, null=True)
    url_img = models.ImageField(blank='', default='', upload_to='img/')
    format_img = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(default=timezone.now)
    edit = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'imgModel'
