from django.contrib import admin
from django.urls import path, include
import content.urls
from django.conf import settings
from django.conf.urls.static import static

app_name = 'content'

urlpatterns = [
    path("", include('content.urls')),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)