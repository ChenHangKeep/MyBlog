import markdown
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.html import strip_tags


#类别
class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="文章分类")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")


    def __str__(self):
        return self.category_name



#标签
class Tag(models.Model):
    tag_name = models.CharField(max_length=100, verbose_name="标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=70, verbose_name="文章标题")
    content = models.TextField(default="", verbose_name="文章内容")
    excerpt = models.CharField(default="", max_length=200,blank=True, verbose_name="摘录")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="文章分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    views = models.PositiveIntegerField(default=0, verbose_name="阅读数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.excerpt:
            # 首先实例化一个Markdown 类 用于渲染content的文本
            md =markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:54]
        super(Article, self).save()

