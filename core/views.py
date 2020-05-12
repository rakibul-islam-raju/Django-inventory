from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import DeptForm, CategotyForm, ProductForm, WarehouseForm
from .models import Department, Category, Product, Warehouse

from django.contrib.auth import get_user_model
User = get_user_model()


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(status=True)
        return context


class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(status=True)
        return context
    

# >=========== create views =============>


class ProductCreateView(View):
    def get(self, *args, **kwargs):
        form = ProductForm()
        context = {
            'form': form,
            'title': 'Add new product'
        }
        return render(self.request, 'product_create.html', context)

    def post(self, *args, **kwargs):
        form = ProductForm(self.request.POST or None)
        added_by = User.objects.get(username=self.request.user.username)
        added_by = added_by.username

        if form.is_valid():
            category = form.cleaned_data.get('category')
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            quantity = form.cleaned_data.get('quantity')
            warehouse = form.cleaned_data.get('warehouse')
            office = self.request.user
            new_dept = Product(category=category, name=name, price=price, description=description, added_by=added_by, quantity=quantity, office=office, warehouse=warehouse)
            new_dept.save()
            messages.success(self.request, 'Product added successfully')
            return redirect('/')
        else:
            messages.warning(self.request, 'Something went wrong')
            return redirect('/')


class DeparmentCreateView(SuccessMessageMixin, CreateView):
    model = Department
    template_name = 'department.html'
    form_class = DeptForm
    success_url = 'core:department'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add new department'
        context["departments"] = Department.objects.filter(status=True)
        return context

    def form_valid(self, form):
        form.instance.office = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'category.html'
    form_class = CategotyForm
    success_url = 'core:category'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add new category'
        context["categories"] = Category.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class WarehouseCreateView(SuccessMessageMixin, CreateView):
    model = Warehouse
    template_name = 'warehouse.html'
    form_class = WarehouseForm
    success_url = 'core:warehouse'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["warehouses"] = Warehouse.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


# >=========== update views =============>


class ProductUpdateView(LoginRequiredMixin ,UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = 'core:home'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit product'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        product = self.get_object()
        if self.request.user.username == product.added_by:
            return True
        return False


class DepartmentUpdateView(LoginRequiredMixin ,UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Department
    form_class = DeptForm
    template_name = 'department.html'
    success_url = 'core:department'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit department'
        context["departments"] = Department.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        department = self.get_object()
        if self.request.user.username == department.office.username:
            return True
        return False


class CategoryUpdateView(LoginRequiredMixin ,UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategotyForm
    template_name = 'category.html'
    success_url = 'core:category'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit category'
        context["categories"] = Category.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
        
    def test_func(self):
        category = self.get_object()
        if self.request.user.username == category.department.office.username:
            return True
        return False


class WarehouseUpdateView(SuccessMessageMixin, UpdateView):
    model = Warehouse
    template_name = 'warehouse.html'
    form_class = WarehouseForm
    success_url = 'core:warehouse'
    success_message = "%(name)s was Updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["warehouses"] = Warehouse.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


# >=================== delete views ===============>


class ProductDeleteView(LoginRequiredMixin ,UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = 'core:home'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        product = self.get_object()
        if self.request.user.username == product.added_by:
            return True
        return False


class DepartmentDeleteView(LoginRequiredMixin ,UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Department
    template_name = 'delete.html'
    success_url = 'core:department'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        department = self.get_object()
        if self.request.user.username == department.office.username:
            return True
        return False


class CategoryDeleteView(LoginRequiredMixin ,UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = 'core:home'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        category = self.get_object()
        if self.request.user.username == category.department.office.username:
            return True
        return False


class WarehouseDeleteView(SuccessMessageMixin, DeleteView):
    model = Warehouse
    template_name = 'warehouse.html'
    success_url = 'core:home'
    success_message = "%(name)s was deleted successfully"
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
