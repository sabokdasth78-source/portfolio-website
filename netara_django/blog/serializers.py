from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField() # برای نمایش آرایه‌ای از تگ‌ها

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'image', 'tags', 'created_at', 'updated_at']
