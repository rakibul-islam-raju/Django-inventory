from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (HomeView,

                    download_product_csv,

                    ProductView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,

                    DeparmentCreateView,
                    DepartmentUpdateView,
                    DepartmentDeleteView,

                    CategoryCreateView,
                    CategoryUpdateView,
                    CategoryDeleteView,

                    WarehouseCreateView,
                    WarehouseUpdateView,
                    WarehouseDeleteView,

                    BankCreateView,
                    BankUpdateView,
                    BankDeleteView,

                    TransactionCreateView,
                    TransactionUpdateView,
                    TransactionDeleteView,
                    )

app_name = 'core'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),

    path('download_product_csv', staff_member_required(download_product_csv), name='product-download-csv'),

    path('product/', staff_member_required(ProductView.as_view()), name='product'),
    path('product/create/', staff_member_required(ProductCreateView.as_view()), name='product-create'),
    path('product/edit/<pk>/', staff_member_required(ProductUpdateView.as_view()), name='product-edit'),
    path('product/delete/<pk>/', staff_member_required(ProductDeleteView.as_view()), name='product-delete'),

    path('department/', staff_member_required(DeparmentCreateView.as_view()), name='department'),
    path('department/<pk>/', staff_member_required(DepartmentUpdateView.as_view()), name='department-edit'),
    path('department/delete/<pk>/', staff_member_required(DepartmentDeleteView.as_view()), name='department-delete'),

    path('category/', staff_member_required(CategoryCreateView.as_view()), name='category'),
    path('category/<pk>/', staff_member_required(CategoryUpdateView.as_view()), name='category-edit'),
    path('category/delete/<pk>/', staff_member_required(CategoryDeleteView.as_view()), name='category-delete'),

    path('warehouse/', staff_member_required(WarehouseCreateView.as_view()), name='warehouse'),
    path('warehouse/<pk>', staff_member_required(WarehouseUpdateView.as_view()), name='warehouse-edit'),
    path('warehouse/delete/<pk>', staff_member_required(WarehouseDeleteView.as_view()), name='warehouse-delete'),

    path('bank/', staff_member_required(BankCreateView.as_view()), name='bank'),
    path('bank/<pk>/', staff_member_required(BankUpdateView.as_view()), name='bank-edit'),
    path('bank/delete/<pk>/', staff_member_required(BankDeleteView.as_view()), name='bank-delete'),
    
    path('transaction/', staff_member_required(TransactionCreateView.as_view()), name='transaction'),
    path('transaction/<pk>/', staff_member_required(TransactionUpdateView.as_view()), name='transaction-edit'),
    path('transaction/delete/<pk>/', staff_member_required(TransactionDeleteView.as_view()), name='transaction-delete'),
]
