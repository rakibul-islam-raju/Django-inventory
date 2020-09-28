from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Customer, SellProduct
from .forms import CustomerForm, SellProductForm
from core.models import User, Product


class SellProductListView(TemplateView):
    template_name = 'sell/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProduct.objects.all()
        return context


class SellProductItem(SuccessMessageMixin, CreateView):
    model = SellProduct
    template_name = 'sell/product-create.html'
    form_class = SellProductForm
    success_url = 'sell:product'
    success_message = "Order was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProduct.objects.all()
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def get(self, *args, **kwargs):
        product_instance = get_object_or_404(Product, pk=self.kwargs['pk'])
        form = SellProductForm(initial={
            'warehouse': product_instance.warehouse,
            'product': product_instance,
            'price': product_instance.sell_price,
            'quantity': product_instance.quantity
            })
        context = {
            'form': form
        }
        return render(self.request, 'sell/product-create.html', context)
        
    def post(self, *args, **kwargs):
        product_instance = get_object_or_404(Product, pk=self.kwargs['pk'])
        form = SellProductForm(self.request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')

            print(quantity)
            print(product_instance.quantity)

            if quantity <= product_instance.quantity:
                new_qntty = product_instance.quantity - quantity
                product_instance.quantity = new_qntty
                product_instance.save(update_fields=['quantity'])

            form.save()
            return redirect('sell:product')


class SellProductCreateView(SuccessMessageMixin, CreateView):
    model = SellProduct
    template_name = 'sell/product-create.html'
    form_class = SellProductForm
    success_url = 'sell:product'
    success_message = "Order was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProduct.objects.all()
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

        
class SellProductUpdateView(SuccessMessageMixin, UpdateView):
    def get(self, *args, **kwargs):
        form = SellProductForm()
        context = {
            'form': form,
            'title': 'Create New Sell',
        }
        return render(self.request, 'sell/product-create.html', context)
    
    def post(self, *args, **kwargs):
        form = SellProductForm(self.request.POST or None)
        # added_by = User.objects.get(username=self.request.user.username)
        # added_by = added_by.username

        if form.is_valid():
            warehouse = form.cleaned_data.get('warehouse')
            customer = form.cleaned_data.get('customer')
            product = form.cleaned_data.get('product')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')

            new_product = SellProduct(warehouse=warehouse, customer=customer, product=product, price=price, description=description, status=status)
            new_product.save()
            messages.success(self.request, 'Sell was Created successfully')
            return redirect('/')
        else:
            messages.warning(self.request, 'Something went wrong')
            return redirect('/')

    # model = SellProduct
    # template_name = 'sell/product-create.html'
    # form_class = SellProductForm
    # success_url = 'sell:product'
    # success_message = "%(name)s was updated successfully"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["products"] = SellProduct.objects.all()
    #     return context

    # def get_success_url(self, **kwargs):
    #     return reverse(self.success_url)


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


class SingleCustomerView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        sellproduct = SellProduct.objects.filter(id=customer.id)
        context = {
            'customer': customer,
            'sellproduct': sellproduct
        }
        return render(self.request, 'sell/single-customer.html', context)
