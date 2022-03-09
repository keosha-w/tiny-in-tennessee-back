from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    title = models.CharField(max_length=50)
    location_category_id = models.OneToOneField(
        "LocationId", on_delete=models.CASCADE, related_name='locations'
    )
    electrical = models.BooleanField(default=True)
    address = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    water = models.BooleanField(default=True)
    septic = models.BooleanField(default=True)
    monthlyPrice = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )