from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Customer, SellProduct
from .forms import CustomerForm, SellProductForm


class SellProductListView(TemplateView):
    template_name = 'sell/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProduct.objects.filter(status=True)
        return context


class SellProductCreateView(SuccessMessageMixin, CreateView):
    model = SellProduct
    template_name = 'sell/product-create.html'
    form_class = SellProductForm
    success_url = 'sell:product'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProduct.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

        
class SellProductUpdateView(SuccessMessageMixin, UpdateView):
    model = SellProduct
    template_name = 'sell/product-create.html'
    form_class = SellProductForm
    success_url = 'sell:product'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProduct.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class SellProductDeleteView(SuccessMessageMixin, DeleteView):
    model = SellProduct
    template_name = 'delete.html'
    success_url = 'sell:product'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    

class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    template_name = 'sell/customer.html'
    form_class = CustomerForm
    success_url = 'sell:customer'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customers"] = Customer.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = Customer
    template_name = 'sell/customer.html'
    form_class = CustomerForm
    success_url = 'sell:customer'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customers"] = Customer.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CustomerDeleteView(SuccessMessageMixin, DeleteView):
    model = Customer
    template_name = 'delete.html'
    success_url = 'sell:customer'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
