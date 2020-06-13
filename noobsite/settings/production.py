from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    # before core apps
] + core_apps + [
    # after core apps
]

DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

MIDDLEWARE = [
    # before core middlewares
] + core_middlewares + [
    # after core middlewares
]

# Activate Django-Heroku.
django_heroku.settings(locals())

try:
    from .local import *
except ImportError:
    pass