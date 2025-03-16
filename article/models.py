from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(max_length=100, verbose_name='名称')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

class ArticleInfo(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    title = models.CharField(max_length=200, verbose_name='标题')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    cover = models.ImageField(upload_to='images/article/cover/', blank=True, null=True, verbose_name='封面')
    desc = models.TextField(verbose_name="描述")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    content = RichTextUploadingField(verbose_name='内容')

    def __str__(self):
        return self.title