from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (SellProductListView,
                    SellProductCreateView,
                    SellProductUpdateView,
                    SellProductDeleteView,
                    SingleCustomerView,

                    CustomerCreateView,
                    CustomerUpdateView,
                    CustomerDeleteView
                    )

app_name = 'sell'

urlpatterns = [
    path('customer/', staff_member_required(CustomerCreateView.as_view()), name='customer'),
    path('customer/<int:pk>/', staff_member_required(SingleCustomerView.as_view()), name='single-customer'),
    path('customer/<pk>/', staff_member_required(CustomerUpdateView.as_view()), name='customer-edit'),
    path('customer/delete/<pk>/', staff_member_required(CustomerDeleteView.as_view()), name='customer-delete'),

    path('sell/create/', staff_member_required(SellProductCreateView.as_view()), name='sell-create'),
    path('sell/edit/<pk>/', staff_member_required(SellProductUpdateView.as_view()), name='sell-edit'),
    path('sell/delete/<pk>/', staff_member_required(SellProductDeleteView.as_view()), name='sell-delete'),
    path('sell/products/', staff_member_required(SellProductListView.as_view()), name='product'),
]
