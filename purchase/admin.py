from django.contrib import admin
from .models import Supplier, PurchaseProduct


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name' , 'phone', 'email', 'status']
    list_display_links = ['name' , 'phone', 'email']
    search_fields = ['name' , 'phone', 'email']

class PurchaseProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price', 'quantity', 'status']
    search_fields = ['name']
    list_filter = ['status']

    date_hierarchy = 'timestamp'


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(PurchaseProduct, PurchaseProductAdmin)
