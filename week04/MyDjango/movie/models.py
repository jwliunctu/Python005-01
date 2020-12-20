from django.db import models

# Create your models here.

class Comment(models.Model):
    # id 自動創建
    author = models.CharField(max_length=20)
    star = models.IntegerField()
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField()