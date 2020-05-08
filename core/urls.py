from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (ProdectListView,
                    ProductCreateView,
                    DeparmentCreateView,
                    CategoryCreateView,
                    ProductUpdateView,
                    DepartmentUpdateView,
                    CategoryUpdateView,
                    ProductDeleteView,
                    DepartmentDeleteView,
                    CategoryDeleteView
                    )

app_name = 'core'

urlpatterns = [
    path('', login_required(ProdectListView.as_view()), name='home'),
    path('product-create/', staff_member_required(ProductCreateView.as_view()), name='product-create'),
    path('department-create/', staff_member_required(DeparmentCreateView.as_view()), name='department-create'),
    path('category-create/', staff_member_required(CategoryCreateView.as_view()), name='category-create'),
    path('product-edit/<pk>/', staff_member_required(ProductUpdateView.as_view()), name='product-edit'),
    path('department-edit/<pk>/', staff_member_required(DepartmentUpdateView.as_view()), name='department-edit'),
    path('category-edit/<pk>/', staff_member_required(CategoryUpdateView.as_view()), name='category-edit'),
    path('product-delete/<pk>/', staff_member_required(ProductDeleteView.as_view()), name='product-delete'),
    path('department-delete/<pk>/', staff_member_required(DepartmentDeleteView.as_view()), name='department-delete'),
    path('category-delete/<pk>/', staff_member_required(CategoryDeleteView.as_view()), name='category-delete'),
]
