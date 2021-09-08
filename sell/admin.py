from django.contrib import admin
from .models import Customer, SellProductItem


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'status']
    list_display_links = ['name', 'phone', 'email']
    search_fields = ['phone', 'email']


# class SellProductItemAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'date_added', 'description']
#     search_fields = ['product', 'customer']

#     date_hierarchy = 'date_added'


admin.site.register(Customer, CustomerAdmin)
admin.site.register(SellProductItem)
