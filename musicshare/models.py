from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

#here are the models firstly for CustomUser

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

class Audio_store(models.Model):
    title=models.CharField(max_length=255)
    CHOICES = [('1', 'Public'), ('2', 'Protected'), ('3', 'Private')]
    privacy = models.CharField(max_length=1,choices=CHOICES,default='1')
    uploaded_by=models.EmailField()
    uploaded_for=models.CharField(max_length=100000,null=True)
    music=models.FileField(upload_to='uploads/')
    class Meta:
        db_table='Audio_store'
#10485760
