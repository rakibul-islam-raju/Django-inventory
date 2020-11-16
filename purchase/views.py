from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (CreateView,
                                ListView,
                                DetailView,
                                UpdateView,
                                DeleteView,
                                TemplateView,
                                View)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import *

from core.models import Product, Organization, Warehouse
from core.forms import CategoryForm, WarehouseForm, SubcategoryForm

import json

# from django.contrib.auth import get_user_model
# User = get_user_model()


class PurchaseProductList(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        TemplateView):
    template_name = 'purchase/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = PurchaseProduct.objects.filter(status=True)
        return context
    
    def test_func(self, *args, **kwargs):
        if self.request.user.is_staff:
            return True
        return False


# class CreateSupplierView(LoginRequiredMixin,
#                         UserPassesTestMixin,
#                         SuccessMessageMixin,
#                         CreateView):
#     model = Supplier
#     template_name = 'purchase/supplier.html'
#     form_class = SupplierForm
#     success_url = 'purchase:supplier'
#     success_message = "%(name)s was created successfully"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["suppliers"] = Supplier.objects.filter(status=True)
#         context["title"] = 'Add New Supplier'
#         return context

#     def get_success_url(self, **kwargs):
#         return reverse(self.success_url)

#     def test_func(self, *args, **kwargs):
#         if self.request.user.is_staff:
#             return True
#         return False


class CreatePurchaseView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        View):
    def get(self, *args, **kwargs):
        form = PurchaseProductForm()
        context = {
            'form': form,
            'title': 'Create New Purchase',
            'warehouse_form': WarehouseForm(),
            'category_form': CategoryForm(),
            'subcategory_form': SubcategoryForm(),
        }
        return render(self.request, 'purchase/product-create.html', context)

    def post(self, *args, **kwargs):
        form = PurchaseProductForm(self.request.POST or None)

        if form.is_valid():
            warehouse = form.cleaned_data.get('warehouse')
            category = form.cleaned_data.get('category')
            sub_category = form.cleaned_data.get('sub_category')
            product_name = form.cleaned_data.get('product_name')
            cost_price = form.cleaned_data.get('cost_price')
            sell_price = form.cleaned_data.get('sell_price')
            quantity = form.cleaned_data.get('quantity')
            payment_type = form.cleaned_data.get('payment_type')
            bank = form.cleaned_data.get('bank')
            check_no = form.cleaned_data.get('check_no')
            check_date = form.cleaned_data.get('check_date')
            remark = form.cleaned_data.get('remark')

            new_purchase = PurchaseProduct(
                warehouse=warehouse,
                category=category,
                sub_category=sub_category,
                product_name=product_name,
                cost_price=cost_price,
                sell_price=sell_price,
                quantity=quantity,
                payment_type=payment_type,
                bank=bank,
                check_no=check_no,
                check_date=check_date,
                remark=remark,
                added_by=self.request.user
            )

            # new_product = Product(
            #     category=category,
            #     warehouse=warehouse,
            #     organization=organization,
            #     name=name,
            #     chalan=chalan,
            #     supplier_price=price,
            #     quantity=quantity,
            #     description=description,
            #     added_by=self.request.user.username
            # )

            new_purchase.save()
            # new_product.save()
            messages.success(self.request, 'Purchase added successfully')
            return redirect('./')
        else:
            messages.warning(self.request, 'Invalid form value. Please try again')
            return redirect('purchase:purchase-create')

    def test_func(self, *args, **kwargs):
        if self.request.user.is_staff:
            return True
        return False


# ============ Detail views ============>

class PurchaseProductDetailView(DetailView):
    model = PurchaseProduct
    template_name = 'purchase-detali.html'

# ============ Update views ============>



class PurchaseProductUpdateView(LoginRequiredMixin,
                                UserPassesTestMixin,
                                SuccessMessageMixin,
                                UpdateView):
    model = PurchaseProduct
    form_class = PurchaseProductForm
    template_name = 'purchase/product-create.html'
    success_url = './'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = PurchaseProduct.objects.filter(status=True)
        context["title"] = 'Edit Purchase'
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self, *args, **kwargs):
        if self.request.user.is_staff:
            return True
        return False


# ================= delete views ==================>


# class SupplireDeleteView(LoginRequiredMixin,
#                         UserPassesTestMixin,
#                         SuccessMessageMixin,
#                         DeleteView):
#     model = Supplier
#     template_name = 'delete.html'
#     success_url = 'purchase:supplier'
#     success_message = "%(name)s was created successfully" 

#     def get_success_url(self, **kwargs):
#         return reverse(self.success_url)

#     def test_func(self):
#         if self.request.user.is_superuser:
#             return True
#         return False


class PurchaseProductDeleteView(LoginRequiredMixin,
                                UserPassesTestMixin,
                                SuccessMessageMixin,
                                DeleteView):
    model = PurchaseProduct
    template_name = 'delete.html'
    success_url = 'purchase:product'
    success_message = "%(name)s was created successfully" 

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
