from django.urls import path, include
from .views import *

app_name = 'purchase'

urlpatterns = [
    # path('supplier/', CreateSupplierView.as_view(), name='supplier'),
    # path('supplier/<pk>/', SupplierUpdateView.as_view(), name='supplier-edit'),
    # path('supplier/delete/<pk>/', SupplireDeleteView.as_view(), name='supplier-delete'),
    
    path('purchase/invoice/<int:pk>/', purchaes_invoice, name='purchase-invoice'),

    path('purchase/create/', CreatePurchaseView.as_view(), name='purchase-create'),
    path('purchase/edit/<pk>/', PurchaseProductUpdateView.as_view(), name='purchase-edit'),
    path('purchase/delete/<pk>/', PurchaseProductDeleteView.as_view(), name='purchase-delete'),
    path('purchase/product/', PurchaseProductList.as_view(), name='product'),
]
