from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    uploaded_by = models.CharField(max_length=128, default='')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')