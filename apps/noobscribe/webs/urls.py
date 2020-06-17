from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage),
    path('accounts/', include('noobscribe.webs.accounts.urls')),
    path('shop/', include('noobscribe.webs.shop.urls')),
]