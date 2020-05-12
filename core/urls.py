from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (HomeView,

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
                    )

app_name = 'core'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),

    path('product/', staff_member_required(ProductView.as_view()), name='product'),
    path('product-create/', staff_member_required(ProductCreateView.as_view()), name='product-create'),
    path('product-edit/<pk>/', staff_member_required(ProductUpdateView.as_view()), name='product-edit'),
    path('product-delete/<pk>/', staff_member_required(ProductDeleteView.as_view()), name='product-delete'),

    path('department/', staff_member_required(DeparmentCreateView.as_view()), name='department'),
    path('department/<pk>/', staff_member_required(DepartmentUpdateView.as_view()), name='department-edit'),
    path('department-delete/<pk>/', staff_member_required(DepartmentDeleteView.as_view()), name='department-delete'),

    path('category/', staff_member_required(CategoryCreateView.as_view()), name='category'),
    path('category/<pk>/', staff_member_required(CategoryUpdateView.as_view()), name='category-edit'),
    path('category-delete/<pk>/', staff_member_required(CategoryDeleteView.as_view()), name='category-delete'),

    path('warehouse/', staff_member_required(WarehouseCreateView.as_view()), name='warehouse'),
    path('warehouse/<pk>', staff_member_required(WarehouseUpdateView.as_view()), name='warehouse-edit'),
    path('warehouse-delete/<pk>', staff_member_required(WarehouseDeleteView.as_view()), name='warehouse-delete'),
]
