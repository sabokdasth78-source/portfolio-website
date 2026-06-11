from django.contrib import admin
from .models import UserRequest

@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'user', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
