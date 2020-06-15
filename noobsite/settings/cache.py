# CACHE
import os

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv('REDIS_URL', 'redis://localhost:6379/2'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": os.getenv('SITE_NAME', 'noobscribe')
    }
}