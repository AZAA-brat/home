from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve as serve_static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]

if settings.DEBUG:
    # Static and uploaded media are served only in development.
    urlpatterns += [path('static/<path:path>', serve_static)]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
