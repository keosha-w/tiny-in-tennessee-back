from distutils.archive_util import make_zipfile
from django.db import models
from django.contrib.auth.models import User

class Law(models.Model):
    county = models.ForeignKey(
        "County", on_delete=models.CASCADE
    )
    zoning = models.CharField(max_length=1000)
    building = models.CharField(max_length=1000)
    notes = models.CharField(max_length=1000)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE 
    )