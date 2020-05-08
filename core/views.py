from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import DeptForm, CategotyForm, ProductForm
from .models import Department, Category, Product


class ProdectListView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(status=True)
        context["departments"] = Department.objects.filter(status=True)
        context["categories"] = Category.objects.filter(status=True)
        return context
    

# >=========== create views =============>


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add new product'
        return context 


class DeparmentCreateView(CreateView):
    model = Department
    template_name = 'product_create.html'
    form_class = DeptForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add new department'
        return context

    # def form_valid(self, form):
        # form.instance.office = self.request.user
        # return super().form_valid(form)


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'product_create.html'
    form_class = CategotyForm
    success_url = 'core:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add new category'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


# >=========== update views =============>


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = 'core:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit product'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DeptForm
    template_name = 'product_create.html'
    success_url = 'core:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit department'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategotyForm
    template_name = 'product_create.html'
    success_url = 'core:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit category'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


# >=================== delete views ===============>


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = 'core:home'

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'delete.html'
    success_url = 'core:home'

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = 'core:home'

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
