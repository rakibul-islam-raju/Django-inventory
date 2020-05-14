from django.contrib import admin
from .models import Customer, SellProduct


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name' , 'phone', 'email', 'status']
    list_display_links = ['name' , 'phone', 'email']
    search_fields = ['name' , 'phone', 'email']


class SellProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price', 'quantity', 'status']
    search_fields = ['name']
    list_filter = ['status']

    date_hierarchy = 'timestamp'


admin.site.register(Customer, CustomerAdmin)
admin.site.register(SellProduct, SellProductAdmin)