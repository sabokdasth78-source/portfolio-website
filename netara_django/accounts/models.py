from django.db import models
from django.contrib.auth.models import User

class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests', null=True, blank=True)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"درخواست {self.full_name}"
