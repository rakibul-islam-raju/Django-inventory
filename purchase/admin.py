from django.contrib import admin
from .models import PurchaseProduct


class PurchaseProductAdmin(admin.ModelAdmin):
    list_display = ['purchase_no',
                    'product',
                    'quantity',
                    'payment_type',
                    'total_price',
                    'status'
                    ]
    search_fields = ['name', 'purchase_no']
    list_filter = ['status', 'payment_type']

    date_hierarchy = 'date_added'


admin.site.register(PurchaseProduct, PurchaseProductAdmin)
