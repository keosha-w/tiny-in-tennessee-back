
from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    title = models.CharField(max_length=50)
    location_category = models.ForeignKey(
        "LocationCategory", on_delete=models.CASCADE, default=None
    )
    electrical = models.BooleanField(default=True)
    address = models.CharField(max_length=100)
    county = models.ForeignKey(
        "County", on_delete=models.CASCADE
    )
    water = models.BooleanField(default=True)
    septic = models.BooleanField(default=True)
    monthlyPrice = models.IntegerField()
    user = models.ForeignKey(
        "TitUser", on_delete=models.CASCADE
    )
    is_approved = models.BooleanField(default=False)