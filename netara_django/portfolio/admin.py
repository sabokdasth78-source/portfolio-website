from django.contrib import admin
from .models import Project, ProjectImage, Article

# کلاس مربوط به آپلود چند تصویر به صورت همزمان در صفحه پروژه
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'technologies')
    inlines = [ProjectImageInline]  # اضافه شدن قابلیت آپلود چندگانه

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)} # ساخت خودکار slug از روی عنوان
    search_fields = ('title',)
