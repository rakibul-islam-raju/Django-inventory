from django.urls import path
from core.api.views import *


urlpatterns = [
    path('warehouse-create', CreateWarehouse.as_view(), name='warehouse-create-api'),
    path('category-create', CreateCategory.as_view(), name='category-create-api'),
    path('subcategory-create', CreateSubcategory.as_view(), name='subcategory-create-api'),
]
