from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    # به جای <slug:slug> از <str:slug> استفاده شده است
    path('posts/<str:slug>/', PostDetailAPIView.as_view(), name='post-detail'),
]
