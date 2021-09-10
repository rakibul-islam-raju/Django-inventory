from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView, ListView, View)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Customer, Sell, SellProductItem
from .forms import CustomerForm, SellForm, SellProductItemForm, SellInlineFormset
from core.models import User, Product


class SellListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    queryset = Sell.objects.filter(status=True)
    template_name = 'sell/sales.html'
    paginate_by = '20'

    def test_func(self, *args, **kwargs):
        if self.request.user.is_staff:
            return True
        return False


class SellProductItem(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    def get(self, *args, **kwargs):
        product_instance = get_object_or_404(Product, pk=self.kwargs['pk'])
        form = SellProductItemForm(initial={
            'warehouse': product_instance.warehouse,
            'product': product_instance,
            'price': product_instance.sell_price,
            'quantity': product_instance.quantity
        })
        context = {
            'form': form,
            'title': 'New Sale'
        }
        return render(self.request, 'sell/product-create.html', context)

    def post(self, *args, **kwargs):
        product_instance = get_object_or_404(Product, pk=self.kwargs['pk'])
        form = SellProductItemForm(self.request.POST or None)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')

            if quantity <= product_instance.quantity:
                new_qntty = product_instance.quantity - quantity
                product_instance.quantity = new_qntty
                product_instance.save(update_fields=['quantity'])
                form.save()
                messages.success(
                    self.request, f'{product_instance.product_name} sold successfully')
                return redirect('sell:sales')
            else:
                messages.warning(self.request, 'Invalid Quantity.')
                return redirect('./')


class SellCreateView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SellProductItem
    template_name = 'sell/product-create.html'
    form_class = SellForm
    success_url = 'sell:sales'
    success_message = "Order was created successfully"

    def post(self, request, *args, **kwargs):
        sell_form = self.get_form_class(request.POST or None)
        sell_item_form = SellProductItemForm(request.POST or None)

        if sell_form.is_valid() and sell_item_form.is_valid():
            # sell = sell_form.cleaned_data.get('sell')
            pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Sale'
        context["sale_item_form"] = SellProductItemForm()
        context["sell_formset"] = SellInlineFormset()
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self, *args, **kwargs):
        if self.request.user.is_staff:
            return True
        return False


class SellProductUpdateView(SuccessMessageMixin, UpdateView):
    model = SellProductItem
    template_name = 'sell/product-create.html'
    form_class = SellProductItemForm
    success_url = 'sell:sales'
    success_message = "%(product)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Sale'
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class SellProductDeleteView(SuccessMessageMixin, DeleteView):
    model = SellProductItem
    template_name = 'delete.html'
    success_url = 'sell:sales'
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


class SingleCustomerView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        sellproduct = SellProduct.objects.filter(id=customer.id)
        context = {
            'customer': customer,
            'sellproduct': sellproduct
        }
        return render(self.request, 'sell/single-customer.html', context)
