from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    