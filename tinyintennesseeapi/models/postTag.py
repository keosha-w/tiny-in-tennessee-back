from django.db import models

class PostTag(models.Model):
    tag_id = models.ManyToManyField(
        "tagId", through='id', related_name='tags'
    )
    post_id = models.ForeignKey("PostId", on_delete=models.CASCADE)