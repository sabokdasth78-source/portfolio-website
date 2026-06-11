from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان پروژه")
    description = models.TextField(verbose_name="توضیحات")
    # فیلد جدید برای عکس دراز صفحه جزئیات:
    mockup_image = models.ImageField(upload_to='projects/mockups/', blank=True, null=True, verbose_name="تصویر کامل (Mockup)")
    
    video = models.FileField(upload_to='projects/videos/', blank=True, null=True, verbose_name="ویدئوی پروژه")
    technologies = models.CharField(max_length=255, help_text="مثال: Django, Vue, Tailwind", verbose_name="تکنولوژی‌های استفاده شده")
    github_link = models.URLField(blank=True, null=True, verbose_name="لینک گیت‌هاب")
    live_link = models.URLField(blank=True, null=True, verbose_name="لینک پیش‌نمایش (Live)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    # ... بقیه کدها بدون تغییر


    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name="پروژه")
    image = models.ImageField(upload_to='projects/images/', verbose_name="تصویر")
    is_featured = models.BooleanField(default=False, verbose_name="تصویر شاخص") # <--- این فیلد اضافه شد

    class Meta:
        verbose_name = "تصویر پروژه"
        verbose_name_plural = "تصاویر پروژه‌ها"

    def __str__(self):
        return f"تصویر {self.project.title}"

class Article(models.Model):
    # ... (کدهای Article بدون تغییر)
    title = models.CharField(max_length=200, verbose_name="عنوان مقاله")
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name="نامک (لینک)")
    content = models.TextField(verbose_name="محتوای مقاله")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="تصویر مقاله")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
