from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    path('', include('purchase.urls', namespace='purchase')),
    path('', include('sell.urls', namespace='sell')),
    path('', include('order.urls', namespace='order')),
    path('users/', include('users.urls', namespace='users')),
]

admin.site.site_header = 'Inventory Admin Panel'
admin.site.index_title = 'Inventory management'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
