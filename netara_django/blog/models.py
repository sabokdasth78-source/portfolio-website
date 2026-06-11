from django.db import models
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True, verbose_name="اسلاگ")
    content = RichTextUploadingField(verbose_name="محتوا")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name="تصویر شاخص")
    tags = TaggableManager(verbose_name="تگ‌ها", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
