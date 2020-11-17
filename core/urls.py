from django.urls import path, include
from core.views import *

app_name = 'core'

urlpatterns = [
    path('api/', include('core.api.urls')),

    path('', HomeView.as_view(), name='home'),

    path('users/', UserManagement.as_view(), name='user-management'),
    path('users/edit/<username>/', EditUserManagent.as_view(), name='edit-user-management'),

    path('download_product_csv', download_product_csv, name='product-download-csv'),

    path('chalan/', ChalanCreateView.as_view(), name='chalan'),
    path('chalan/<int:pk>/', ChalanDetailView.as_view(), name='chalan-detail'),
    path('chalan-edit/<int:pk>/', ChalanUpdateView.as_view(), name='chalan-edit'),
    path('chalan-delete/<int:pk>/', ChalanDeleteView.as_view(), name='chalan-delete'),

    path('product/', ProductView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/edit/<pk>/', ProductUpdateView.as_view(), name='product-edit'),
    path('product/delete/<pk>/', ProductDeleteView.as_view(), name='product-delete'),

    path('department/', CategoryCreateView.as_view(), name='category'),
    path('department/<pk>/', CategoryUpdateView.as_view(), name='category-edit'),
    path('department/delete/<pk>/', CategoryDeleteView.as_view(), name='category-delete'),

    path('category/', SubCategoryCreateView.as_view(), name='subcategory'),
    path('category/<pk>/', SubCategoryUpdateView.as_view(), name='subcategory-edit'),
    path('category/delete/<pk>/', SubCategoryDeleteView.as_view(), name='subcategory-delete'),

    path('warehouse/', WarehouseCreateView.as_view(), name='warehouse'),
    path('warehouse/<pk>', WarehouseUpdateView.as_view(), name='warehouse-edit'),
    path('warehouse/delete/<pk>', WarehouseDeleteView.as_view(), name='warehouse-delete'),

    path('bank/', BankCreateView.as_view(), name='bank'),
    path('bank/<pk>/', BankUpdateView.as_view(), name='bank-edit'),
    path('bank/delete/<pk>/', BankDeleteView.as_view(), name='bank-delete'),
    
    path('transaction/', TransactionCreateView.as_view(), name='transaction'),
    path('transaction/<pk>/', TransactionUpdateView.as_view(), name='transaction-edit'),
    path('transaction/delete/<pk>/', TransactionDeleteView.as_view(), name='transaction-delete'),
]
