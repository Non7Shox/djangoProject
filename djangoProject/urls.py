from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject import settings
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('', include('homepage.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
