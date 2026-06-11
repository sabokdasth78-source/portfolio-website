from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# ایمپورت‌های اضافه شده برای بخش پیام‌ها
from .models import UserRequest
from django.utils.timezone import localtime

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'Registration successful'}, status=201)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful',
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'username': user.username
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    
    if not old_password or not new_password:
        return Response({'error': 'وارد کردن رمز عبور فعلی و جدید الزامی است.'}, status=400)
        
    if not user.check_password(old_password):
        return Response({'error': 'رمز عبور فعلی اشتباه است.'}, status=400)
        
    user.set_password(new_password)
    user.save()
    
    return Response({'message': 'رمز عبور با موفقیت تغییر کرد.'}, status=200)

@api_view(['GET', 'POST'])
def handle_requests(request):
    if request.method == 'POST':
        user = request.user if request.user.is_authenticated else None
        
        # ذخیره درخواست در دیتابیس
        UserRequest.objects.create(
            user=user,
            full_name=request.data.get('full_name'),
            phone=request.data.get('phone'),
            email=request.data.get('email', ''),
            description=request.data.get('description')
        )
        return Response({'message': 'پیام شما با موفقیت ثبت شد.'}, status=201)
        
    elif request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({'error': 'Unauthorized'}, status=401)
            
        # دریافت پیام‌های کاربر و مرتب‌سازی از جدید به قدیم
        requests = UserRequest.objects.filter(user=request.user).order_by('-created_at')
        
        data = [{
            'id': req.id,
            'description': req.description,
            'date': localtime(req.created_at).strftime('%Y-%m-%d %H:%M')
        } for req in requests]
        
        return Response(data, status=200)
