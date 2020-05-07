from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (ProdectListView,
                    ProductCreateView,
                    DeparmentCreateView,
                    CategoryCreateView
                    )

app_name = 'core'

urlpatterns = [
    path('', login_required(ProdectListView.as_view()), name='home'),
    path('product-create/', staff_member_required(ProductCreateView.as_view()), name='product-create'),
    path('department-create/', DeparmentCreateView.as_view(), name='department-create'),
    path('category-create/', CategoryCreateView.as_view(), name='category-create'),
]
