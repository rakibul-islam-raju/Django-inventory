from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from .resources import ProductResource
from .models import Office, Department, Category, Product, User, Warehouse


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def make_status_active(modeladmin, request, queryset):
        queryset.update(status=True)

    def make_status_inactive(modeladmin, request, queryset):
        queryset.update(status=False)

    make_status_active.short_description = 'Update status to active'
    make_status_inactive.short_description = 'Update status to inactive'

    list_display = ['name', 'category', 'price', 'quantity', 'added_by', 'office', 'status']
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


class CategoryAdmin(admin.StackedInline):
    model = Category
    inlines = [ProductAdmin]


admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Warehouse)
# admin.site.register(User)