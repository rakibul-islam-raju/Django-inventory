from django.contrib import admin
from .models import Office, Department, Category, Product

def make_status_active(modeladmin, request, queryset):
    queryset.update(status=True)

def make_status_inactive(modeladmin, request, queryset):
    queryset.update(status=False)

make_status_active.short_description = 'Update status to active'
make_status_inactive.short_description = 'Update status to inactive'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'owner', 'status']
    date_hierarchy = 'timestamp'
    list_display_links = ['name', 'owner']
    search_fields = ['name']
    actions = [make_status_active, make_status_inactive]


admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)