from django.urls import path, include
from django.shortcuts import HttpResponse

def homepage(request):
    return HttpResponse('Homepage Here')

urlpatterns = [
    path('', homepage, name='home_page')
]