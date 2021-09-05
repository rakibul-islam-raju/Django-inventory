from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Inventory Management System",
        default_version='v1',
        description="All available APIs.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rakibul.islam7772588@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    path('api/v1/', include('core.api.urls', namespace='core_api')),
    path('api/v1/', include('purchase.api.urls', namespace='purchase_api')),
    path('api/v1/', include('sell.api.urls', namespace='sell_api')),

    path('', include('core.urls', namespace='core')),
    path('', include('purchase.urls', namespace='purchase')),
    path('', include('sell.urls', namespace='sell')),
    path('', include('order.urls', namespace='order')),
    path('users/', include('users.urls', namespace='users')),
]

admin.site.site_header = 'Inventory Admin Panel'
admin.site.index_title = 'Inventory management'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
