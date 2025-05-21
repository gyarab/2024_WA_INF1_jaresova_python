from django.contrib import admin
from django.urls import path, include
import content.urls
from django.conf import settings
from django.conf.urls.static import static
from content.views import login_view, logout_view, register_view

app_name = 'content'

urlpatterns = [
    path("", include('content.urls')),
    path("admin/", admin.site.urls),
    path("login", login_view, name="login"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path("logout", logout_view, name="logout"),
    path("register", register_view, name="register"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)