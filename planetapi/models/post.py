from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=512)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name= "post_category")
    date = models.DateField(auto_now_add=True)
    image = models.CharField(max_length=513)
    author = models.ForeignKey("Author", on_delete= models.CASCADE, related_name= "post_author")
