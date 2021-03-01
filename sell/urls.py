from django.urls import path, include
from .views import *

app_name = 'sell'

urlpatterns = [
    path('sell/product/<int:pk>', SellProductItem.as_view(), name='sell-product'),

    path('customer/', CustomerCreateView.as_view(), name='customer'),
    path('customer/<int:pk>/', SingleCustomerView.as_view(), name='single-customer'),
    path('customer/edit/<int:pk>/', CustomerUpdateView.as_view(), name='customer-edit'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer-delete'),

    path('sell/create/', SellProductCreateView.as_view(), name='sell-create'),
    path('sell/edit/<pk>/', SellProductUpdateView.as_view(), name='sell-edit'),
    path('sell/delete/<pk>/', SellProductDeleteView.as_view(), name='sell-delete'),
    path('sell/products/', SellProductListView.as_view(), name='product'),
]
