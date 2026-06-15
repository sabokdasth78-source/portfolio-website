from pathlib import Path
from datetime import timedelta
import mimetypes
mimetypes.add_type("video/mp4", ".mp4", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)uc^38pyf*7&q*skx*k@pdwg369fv#ztcob_1-f@z0fp_2f$gv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # برای امنیت سرور حتما باید False باشد

# آدرس ساب‌دامین بک‌اند خود را اینجا وارد کنید (لوکال‌هاست برای تست نگه داشته شده است)
ALLOWED_HOSTS = ['api.netaraweb.ir', 'www.api.netaraweb.ir', 'localhost', '127.0.0.1']

# این گزینه حذف شد زیرا در پروداکشن نباید به همه اجازه دسترسی داد.
# کنترل دسترسی از طریق CORS_ALLOWED_ORIGINS انجام می‌شود.


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'accounts',
    'portfolio',
    'blog',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
]

# تنظیمات مربوط به آپلود عکس در میان متن
CKEDITOR_UPLOAD_PATH = "blog_content_images/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# آدرس فرانت‌اند (ناکست) شما که اجازه دارد به این بک‌اند درخواست بفرستد
CORS_ALLOWED_ORIGINS = [
    "https://netaraweb.ir",
    "https://www.netaraweb.ir",
    "http://localhost:3000", # نگه داشته شده برای تست احتمالی
]

ROOT_URLCONF = 'netara_django.urls'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'netara_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
# این خط برای اعمال CSS ها در پنل ادمین هنگام آپلود روی هاست ضروری است
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  # توکن 1 روز اعتبار داره
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # توکن تمدید 7 روز
}
