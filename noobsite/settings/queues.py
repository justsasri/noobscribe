"""
    Django RQ Configuration
"""
import os

RQ_SHOW_ADMIN_LINK = True

RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDIS_QUEUE_URL', 'redis://localhost:6379/0'), # If you're on Heroku
        'DEFAULT_TIMEOUT': 500,
    },
    'high': {
        'URL': os.getenv('REDIS_QUEUE_URL', 'redis://localhost:6379/0'), # If you're on Heroku
        'DEFAULT_TIMEOUT': 500,
    },
    'mail': {
        'URL': os.getenv('REDIS_QUEUE_URL', 'redis://localhost:6379/0'), # If you're on Heroku
        'DEFAULT_TIMEOUT': 500,
    },
}

# If you need custom exception handlers
# RQ_EXCEPTION_HANDLERS = ['path.to.my.handler'] 