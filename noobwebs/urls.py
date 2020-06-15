from django.urls import path, include

urlpatterns = [
    path('', include('noobwebs.core.urls')),
    path('accounts/', include('noobwebs.accounts.urls')),
    path('shop/', include('noobwebs.shop.urls')),
]