"""timetable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# docs_urlpatterns = [
#     path('', SpectacularAPIView.as_view(), name='schema'),
#     path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
#     path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]

api_urlpatterns = [
    path('admin-site/', include('admin_site.urls')),
    path('', include('retail_site.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    # path('docs/', include(docs_urlpatterns)),
    path('docs/schema/', SpectacularAPIView.as_view(api_version='YOUR_VERSION'), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
