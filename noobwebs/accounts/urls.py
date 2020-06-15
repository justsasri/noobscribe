from django.urls import path, include
from allauth import urls as allauth_urls
from django.shortcuts import HttpResponse, render


def home(request):
    return HttpResponse('home')

def profile(request):
    return render(request, 'accounts/index.html')

urlpatterns = [
    path('', home),
    path('profile/', profile),
]


urlpatterns += allauth_urls.urlpatterns