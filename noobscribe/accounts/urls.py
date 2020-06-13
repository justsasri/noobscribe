from django.urls import path, include
from allauth import urls as allauth_urls
from django.shortcuts import HttpResponse


def profile(request):
    return HttpResponse('Profile')


urlpatterns = [
    path('profile/', profile),
]


urlpatterns += allauth_urls.urlpatterns