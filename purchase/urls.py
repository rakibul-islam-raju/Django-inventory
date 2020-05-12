from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (CreateSupplierView,
                    SupplierUpdateView,
                    SupplireDeleteView,

                    CreatePurchaseView,
                    PurchaseProductList,
                    # PurchaseProductUpdateView,
                    PurchaseProductDeleteView,
                    )

app_name = 'purchase'

urlpatterns = [
    path('supplier/', staff_member_required(CreateSupplierView.as_view()), name='supplier'),
    path('supplier/<pk>/', staff_member_required(SupplierUpdateView.as_view()), name='supplier-edit'),
    path('supplier/delete/<pk>/', staff_member_required(SupplireDeleteView.as_view()), name='supplier-delete'),
    
    path('purchase/create/', staff_member_required(CreatePurchaseView.as_view()), name='purchase-create'),
    # path('purchase/edit/<pk>/', staff_member_required(PurchaseProductUpdateView.as_view()), name='purchase-edit'),
    path('purchase/delete/<pk>/', staff_member_required(PurchaseProductDeleteView.as_view()), name='purchase-delete'),
    path('purchase/products/', staff_member_required(PurchaseProductList.as_view()), name='product'),
]
