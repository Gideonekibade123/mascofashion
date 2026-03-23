from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-v!t@hv#ko1_t3jyq&b33-$@15%b)c&r$ukmj+jkzd-_ur346)z'
DEBUG = False
ALLOWED_HOSTS = ['mascofashion.onrender.com',]


# Paystack credentials
PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")




    # Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_rest_passwordreset',

    # Your apps
    'masco.payments', 
    'masco.users',
    'masco.shop',
]

# Use your custom user model
#AUTH_USER_MODEL = 'users.CustomUser'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'masco.urls'

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

WSGI_APPLICATION = 'masco.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & Media
STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# DEFAULT_FROM_EMAIL = "noreply@example.com"




# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gekibade@gmail.com'
EMAIL_HOST_PASSWORD = 'qtdxoikqlwlphnkq'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'noreply@example.com'

# Frontend URL
FRONTEND_URL = 'https://reacte-commerceproject.netlify.app/'

# CORS
CORS_ALLOWED_ORIGINS = ["https://reacte-commerceproject.netlify.app",]
CORS_ALLOW_ALL_ORIGINS = False  # only for development

# "http://localhost:5173"

# DRF & JWT
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# Default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'