from .base import *
from .auth import *
from .queues import *
from .cache import *


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

# MEDIA FILES

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = os.getenv('AWS_S3_CUSTOM_DOMAIN')
AWS_LOCATION=os.getenv('AWS_LOCATION')
AWS_S3_ENDPOINT_URL=os.getenv('AWS_S3_ENDPOINT_URL')

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Activate Django-Heroku.
django_heroku.settings(locals())

try:
    from .local import *
except ImportError:
    pass