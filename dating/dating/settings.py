"""
Django settings for dating project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import dotenv
from urllib.parse import quote
from pathlib import Path


dotenv.load_dotenv(os.path.join(r'D:\DjangoProjects\Dating-site\venv', '.env'))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'daphne',
    'chats.apps.ChatsConfig',
    'accounts.apps.AccountsConfig',
    'members.apps.MembersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'easy_thumbnails',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'dating.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'dating.wsgi.application'
ASGI_APPLICATION = 'dating.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dating',
        'USER': 'postgres',
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# auth user model

AUTH_USER_MODEL = 'accounts.DatingUser'

# media

MEDIA_URL = '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR, "media")

# Email backend

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# iternal ips

INTERNAL_IPS = [
    '127.0.0.1',
]

# Login/out auth

LOGIN_REDIRECT_URL = 'user_detail'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


# Redis / channels

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6380
REDIS_DB = 0
REDIS_USER = os.environ['REDIS_USER']
REDIS_USER_PASSWORD = os.environ['REDIS_USER_PASSWORD']

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [f'redis://{REDIS_USER}:{quote(REDIS_USER_PASSWORD)}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'],
        },
    },
}

# Celery conf

CELERY_BROKER_URL = f'amqp://suser_rabbitmq:{quote(os.environ['RABBITMQ_PASSWORD'])}@127.0.0.1:5672/'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
