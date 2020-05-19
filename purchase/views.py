from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Supplier, PurchaseProduct
from .forms import SupplierForm, PurchaseProductForm

# from django.contrib.auth import get_user_model
# User = get_user_model()


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
        context["title"] = 'Add New Supplier'
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CreatePurchaseView(SuccessMessageMixin, View):
    def get(self, *args, **kwargs):
        form = PurchaseProductForm()
        context = {
            'form': form,
            'title': 'Create New Purchase'
        }
        return render(self.request, 'purchase/product-create.html', context)

    def post(self, *args, **kwargs):
        form = PurchaseProductForm(self.request.POST or None)
        # added_by = User.objects.get(username=self.request.user.username)
        # added_by = added_by.username

        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            quantity = form.cleaned_data.get('quantity')
            description = form.cleaned_data.get('description')
            warehouse = form.cleaned_data.get('warehouse')
            supplier = form.cleaned_data.get('supplier')
            
            new_purchase = PurchaseProduct(name=name, price=price, quantity=quantity, description=description, warehouse=warehouse, supplier=supplier)
            new_purchase.save()
            messages.success(self.request, 'Purchase added successfully')
            return redirect('purchase:product')
        else:
            messages.warning(self.request, 'Invalid form value. Please try again')
            return redirect('purchase:purchase-create')


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
        context["title"] = 'Edit Supplier'
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    

class PurchaseProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PurchaseProduct
    form_class = PurchaseProductForm
    template_name = 'purchase/product-create.html'
    success_url = 'purchase:product'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = PurchaseProduct.objects.filter(status=True)
        context["title"] = 'Edit Product'
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
