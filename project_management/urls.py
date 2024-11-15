# project_management/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),       # Users app URLs
    path('api/projects/', include('projects.urls')), # Projects app URLs
    path('api/tasks/', include('tasks.urls')),       # Tasks app URLs

    # Swagger and Redoc URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Serve favicon.ico
from django.views.generic import RedirectView
urlpatterns += [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico'))
]