from distutils.archive_util import make_zipfile
from django.db import models
from django.contrib.auth.models import User

class Law(models.Model):
    county = models.CharField(max_length=50)
    zoning = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    notes = models.CharField(max_length=1000)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE 
    )