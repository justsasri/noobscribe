import time
from django.urls import path, include
from . import views

def long_running_time(text):
    time.sleep(10)
    print(text)
    return 'done'

def test_time(request, some_text):
    from django.http import HttpResponse
    import django_rq
    queue = django_rq.get_queue('default')
    queue.enqueue(long_running_time, some_text)
    return HttpResponse()

urlpatterns = [
    path('user/<str:user_id>', views.user_detail),
    path('fun/<str:some_text>', test_time)
]