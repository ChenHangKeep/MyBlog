from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from blog.models import Article

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="文章")
    text = models.CharField(max_length=200,default="", verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return self.user