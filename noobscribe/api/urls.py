from django.urls import path, include

urlpatterns = [
    path('rest_v1/', include('noobscribe.api.rest_v1.urls')),
]