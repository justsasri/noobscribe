"""
Django settings for noobsite project.

"""
import os
import environ
import django_heroku
import dj_database_url

from .auth import *
from .queues import *
from .cache import *

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SITE_ID = 1
SITE_NAME = 'noobscribe'
BASE_URL = 'https://www.noobscibe.com'
SECRET_KEY = os.getenv("SECRET_KEY", "i&sof=vxv%z15h89yh8dk-@t!!y&7-(y+n1cm@on!-fl=nu3$9")


# Apps definition

core_apps = [

    'noobscribe.auth',
    'noobscribe.core',
    'noobscribe.plans',
    'noobscribe.sales',
    'noobscribe.api.rest_v1',

    'noobwebs.core',
    'noobwebs.accounts',
    'noobwebs.shop',

    'django_numerators',
    'django_rq',
    'rest_framework',
    'polymorphic',
    'taggit',
    'mptt',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Provider
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

core_middlewares = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'noobsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
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

WSGI_APPLICATION = 'noobsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# Default Django Staticfiles Storage
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
            'propagate': True,
        },
        "rq.worker": {
            "handlers": ["rq_console", "sentry"],
            "level": "DEBUG"
        },
    },
}