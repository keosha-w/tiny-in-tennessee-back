from django.db import models
from django.contrib.auth.models import User

class Builder(models.Model):
    title = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE 
    )
    