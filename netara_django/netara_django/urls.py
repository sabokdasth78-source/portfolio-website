from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/', include('portfolio.urls')),
    path('api/blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    # تنظیمات سرو فایل‌های رسانه (Media) و استاتیک (Static) در محیط پروداکشن (هاست)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
