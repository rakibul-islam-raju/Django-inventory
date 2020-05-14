from import_export import resources
from .models import Department, Category, Product


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
        fields = ['name', 'category', 'supplier_price', 'sell_price', 'added_by', 'status', 'description']
