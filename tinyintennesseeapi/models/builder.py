from django.db import models
from django.contrib.auth.models import User

class Builder(models.Model):
    title = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    user = models.ForeignKey(
        "TitUser", on_delete=models.CASCADE 
    )
    is_approved = models.BooleanField(default=False)