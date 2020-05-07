from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView
from .forms import OfficeForm, DeptForm, CategotyForm, ProductForm
from .models import Office, Department, Category, Product


class ProdectListView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(status=True)
        context["departments"] = Department.objects.filter(status=True)
        context["categories"] = Category.objects.filter(status=True)
        return context
    


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = '/'

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
