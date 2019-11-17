"""
Django settings for VRWare project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from configparser import RawConfigParser
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q*c06+=)tz%pcs=a5#*mcx&@zg$pmle-cdy*lxjgxq9ydgd=vi'

# SECURITY WARNING: don't run with debug turned on in production!
# NOTE: 'False' removes styles from django-admin
DEBUG = True # True by default. Needed to change it to False so that we can see what a live site would show 

# was [] by default. Needed to change to 127.0.0.1 when we changed Debug to False
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'profile', 
    'audioanalysis', 
]

# Removed 'django.middleware.csrf.CsrfViewMiddleware', (https://stackoverflow.com/a/22812799/9599554)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VRWare.urls'
print("BASES", BASE_DIR)
# needed to add 'templates' so that Django will know to look for the new templates folder
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'profile/templates')],
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

WSGI_APPLICATION = 'VRWare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

config = RawConfigParser()
config.read('/home/logan/settings.ini')

DJANGO_ENGINE = config.get('database', 'database_engine')
DJANGO_NAME = config.get('database', 'database_name')
DJANGO_USER = config.get('database', 'database_user')
DJANGO_PASSWORD = config.get('database', 'database_password')
DJANGO_HOST = config.get('database', 'database_host')
DJANGO_PORT = config.get('database', 'database_port')

DATABASES = {
    'default': {
        'ENGINE': DJANGO_ENGINE, 
        'NAME': DJANGO_NAME, 
        'USER': DJANGO_USER, 
        'PASSWORD': DJANGO_PASSWORD, 
        'HOST': DJANGO_HOST, 
        'PORT': DJANGO_PORT
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10
}

# For file uploads
# The location of the iploaded file will be in MEDIA_ROOT/images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# I don't think this is neeeed
MEDIA_URL = '/media/'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# https://stackoverflow.com/questions/35032159/how-to-set-simple-password-in-django-1-9/35032185
"""
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
"""


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, 
    'handlers': {
        'file': {
            'level': 'DEBUG', 
            'class': 'logging.FileHandler',
            'filename': '/home/logan/FCRWebApp/Backend/logs/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level':os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    },
}