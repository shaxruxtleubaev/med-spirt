import os
from pathlib import Path
from datetime import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'django-insecure-^rhh=m$paxy8c2-@_&^=#40@^r&kg&k+r^r-(9@3rk*m3p87%e'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', #Third party
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'modeltranslation',
    'django.contrib.admin',

    # Local
    'app',

    # Third party
    'django_cleanup.apps.CleanupConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',
    'image_optimizer'
]

# Third party
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5500',
]
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5500',
]
CORS_ORIGIN_ALLOW_ALL = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=36500),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=73000),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # Third party
    'whitenoise.middleware.WhiteNoiseMiddleware', # Third party
    'corsheaders.middleware.CorsMiddleware', # Third party
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'
USE_L10N = True
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage'
    }
}

OPTIMIZED_IMAGE_METHOD = 'pillow'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1

TELEGRAM_BOT_TOKEN = '6567575067:AAFEe-bYl-Rk_ZY7fATjNLZQ9vaJbisqDDo'
TELEGRAM_CHAT_ID = '-970033814'

LANGUAGES = [
    ('ru', 'Russia'),
    ('uz', 'Uzbek')
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_LANGUAGES = ('ru', 'uz')
