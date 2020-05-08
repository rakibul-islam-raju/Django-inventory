from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from .resources import ProductResource
from .models import Department, Category, Product, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'office')
    list_filter = ('is_staff', 'is_superuser')


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def make_status_active(modeladmin, request, queryset):
        queryset.update(status=True)

    def make_status_inactive(modeladmin, request, queryset):
        queryset.update(status=False)

    make_status_active.short_description = 'Update status to active'
    make_status_inactive.short_description = 'Update status to inactive'

    list_display = ['name', 'price', 'owner', 'status']
    date_hierarchy = 'timestamp'
    list_display_links = ['name', 'owner']
    search_fields = ['name']
    actions = [make_status_active, make_status_inactive]

    resource_class = ProductResource


admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.register(User)
admin.site.register(User, UserAdmin)