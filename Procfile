release: bash ./release_task.sh
web: gunicorn noobsite.wsgi
worker: python manage.py rqworker high mail default