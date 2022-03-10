from django.db import models

class LocationCategory(models.Model):
    name = models.CharField(max_length=100)
