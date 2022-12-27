from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40,unique=True)

class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    reated_at = models.DateTimeField(
        auto_now_add=True)

