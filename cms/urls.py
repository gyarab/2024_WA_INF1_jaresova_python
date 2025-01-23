from django.contrib import admin
from django.urls import path, include
import content.urls

app_name = 'content'

urlpatterns = [
    path("", include('content.urls')),
    path("admin/", admin.site.urls),
]
