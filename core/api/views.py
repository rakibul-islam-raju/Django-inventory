from rest_framework.generics import CreateAPIView, ListCreateAPIView
from core.models import Warehouse, Category, Subcategory
from core.api.serializers import *


class CreateWarehouse(ListCreateAPIView):
    model = Warehouse
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.filter(status=True)


class CreateCategory(ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=True)


class CreateSubcategory(ListCreateAPIView):
    model = Subcategory
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.filter(status=True)
