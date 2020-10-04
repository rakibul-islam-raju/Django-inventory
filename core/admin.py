from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from .resources import ProductResource
from .models import *


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def make_status_active(self, modeladmin, request, queryset):
        queryset.update(status=True)

    def make_status_inactive(self, modeladmin, request, queryset):
        queryset.update(status=False)

    make_status_active.short_description = 'Update status to active'
    make_status_inactive.short_description = 'Update status to inactive'

    list_display = ['name',
                    'category',
                    'supplier_price',
                    'sell_price',
                    'quantity',
                    'added_by',
                    'office',
                    'status']
    date_hierarchy = 'timestamp'
    list_display_links = ['name', 'added_by']
    search_fields = ['name']
    actions = [make_status_active, make_status_inactive]

    resource_class = ProductResource


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'office', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')


# class UserInlineAdmin():
#     model = User
#     inlines = [ProductAdmin]


class CategoryAdmin(admin.ModelAdmin):
    # model = Category
    list_display = ['name', 'department', 'status']
    list_filter = ['department']
    search_fields = ['name']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'office', 'status']
    list_filter = ['office']
    search_fields = ['name']


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status']
    search_fields = ['name']


class BankAdmin(admin.ModelAdmin):
    list_display = ['name', 'ac_name', 'ac_number', 'branch', 'status']
    search_fields = ['name', 'ac_name', 'ac_number', 'branch']
    list_filter = ['branch']


class BankTransactionAdmin(admin.ModelAdmin):
    list_display = ['account_type', 'transaction_type', 'amount', 'bank', 'date', 'status']
    list_filter = ['account_type', 'transaction_type', 'bank', 'date', 'status']
    date_hierarchy = 'date'


admin.site.register(Chalan)
admin.site.register(Office)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(BankTransaction, BankTransactionAdmin)