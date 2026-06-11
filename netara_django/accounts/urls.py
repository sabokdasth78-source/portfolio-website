from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('change-password/', views.change_password, name='change_password'),
    path('requests/', views.handle_requests, name='requests'),
]
