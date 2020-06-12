from .base import *

env = environ.Env(
    SECRET_KEY=(str, 'i&sof=vxv%z15h89yh8dk-@t!!y&7-(y+n1cm@on!-fl=nu3$9'),
    AWS_STORAGE_BUCKET_NAME=(str, ""),
    AWS_ACCESS_KEY_ID=(str, ''),
    AWS_SECRET_ACCESS_KEY=(str, ""),
    AWS_S3_CUSTOM_DOMAIN=(str, ""),
    REDIS_URL=(str, "")
)

environ.Env.read_env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*.noobscribe.com']

INSTALLED_APPS = [
    'noobscribe.accounts',
    'noobscribe.core'
] + core_apps + [
    # after core apps
]

DATABASES['default'].update(dj_database_url.config(conn_max_age=500, ssl_require=True))

MIDDLEWARE = [
    # before core apps
] + core_middlewares + [
    # after core apps
]

# Activate Django-Heroku.
django_heroku.settings(locals())

try:
    from .local import *
except ImportError:
    pass