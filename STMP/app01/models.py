from django.db import models

# Create your models here.
class Userinfo(models.Model):
     name = models.CharField(max_length=32)
     password = models.CharField(max_length=64)
     is_live = models.BooleanField(default=0)
     token = models.CharField(max_length=256)