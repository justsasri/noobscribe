from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i&sof=vxv%z15h89yh8dk-@t!!y&7-(y+n1cm@on!-fl=nu3$9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'noobscribe.accounts',
    'noobscribe.core'
] + core_apps + [
    # after core apps
]

MIDDLEWARE = [
    # before core apps
] + core_middlewares + [
    # after core apps
]

# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Activate Django-Heroku.
django_heroku.settings(locals())


try:
    from .local import *
except ImportError:
    pass