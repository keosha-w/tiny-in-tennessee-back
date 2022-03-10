from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "TitUser", on_delete=models.CASCADE
    )
    is_approved = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        "Tag", through='PostTag', related_name='tags'
    )