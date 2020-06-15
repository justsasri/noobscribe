"""
    Noobsite URL Configuration
"""

from django.conf import settings
from django.urls import path, include
from noobwebs import urls as web_urls
from noobscribe.api import urls as api_urls

urlpatterns = [
    path('api/', include(api_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.contrib import admin
    
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/', admin.site.urls),
        path('admin/queues/', include('django_rq.urls'))
    ]

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('', include(web_urls)),
]