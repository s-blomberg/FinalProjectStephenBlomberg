from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inventory/', include('inventory.urls')),
    path('maintenance_logs/', include('maintenance_logs.urls')),
    path('weather/', include('weather.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)