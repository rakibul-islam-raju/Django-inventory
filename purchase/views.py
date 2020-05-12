from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Supplier, PurchaseProduct
from .forms import SupplierForm, PurchaseProductForm


class PurchaseProductList(SuccessMessageMixin, TemplateView):
    template_name = 'purchase/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = PurchaseProduct.objects.filter(status=True)
        return context


class CreateSupplierView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    template_name = 'purchase/supplier.html'
    form_class = SupplierForm
    success_url = 'purchase:supplier'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suppliers"] = Supplier.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CreatePurchaseView(SuccessMessageMixin, CreateView):
    model = PurchaseProduct
    form_class = PurchaseProductForm
    template_name = 'purchase/product-create.html'
    success_url = 'purchase:product'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = PurchaseProduct.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


# ============ Update views ============>


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'purchase/supplier.html'
    success_url = 'purchase:supplier'
    success_message = "%(name)s was updated successfully" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suppliers"] = Supplier.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    

class PurchaseProductUpdateView(SuccessMessageMixin, UpdateView):
    model = PurchaseProduct
    form_class = PurchaseProductForm
    template_name = 'purchase/product-create.html'
    success_url = 'purchase:product'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = PurchaseProduct.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


# ================= delete views ==================>


class SupplireDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Supplier
    template_name = 'delete.html'
    success_url = 'purchase:supplier'
    success_message = "%(name)s was created successfully" 

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class PurchaseProductDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PurchaseProduct
    template_name = 'delete.html'
    success_url = 'purchase:product'
    success_message = "%(name)s was created successfully" 

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
