from django.db import models

class PostTag(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_tag")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, related_name="post_tag")