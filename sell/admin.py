from django.contrib import admin
from .models import Customer, Sell, SellProductItem


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'status']
    list_display_links = ['name', 'phone', 'email']
    search_fields = ['phone', 'email']


class SellAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'customer', 'is_sold', 'total_price']
    search_fields = ['invoice_number']
    date_hierarchy = 'date_added'
    readonly_fields = ['total_price']


# class SellProductItemAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'date_added', 'description']
#     search_fields = ['product', 'customer']

#     date_hierarchy = 'date_added'


admin.site.register(Customer, CustomerAdmin)
admin.site.register(SellProductItem)
admin.site.register(Sell, SellAdmin)
