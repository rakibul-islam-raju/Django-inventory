from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (View,
                                ListView,
                                CreateView,
                                UpdateView,
                                DeleteView,
                                TemplateView,
                                DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import (Department,
                    Category,
                    Product,
                    Warehouse,
                    Bank,
                    BankTransaction,
                    Chalan)
from .forms import (DeptForm,
                    CategoryForm,
                    ProductForm,
                    WarehouseForm,
                    BankForm,
                    BankTransactionForm,
                    UserPermissionForm,
                    ChalanCreateForm)
from sell.models import Customer, SellProduct
from purchase.models import Supplier, PurchaseProduct
from .resources import ProductResource
from .filters import ChalanFilter

from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required()
def download_product_csv(request):
    product_resource = ProductResource()
    dataset = product_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    return response


class HomeView(LoginRequiredMixin,
            TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(status=True)
        context["products"] = products

        context["total_products"] = products.count()
        context["total_customer"] = Customer.objects.filter(status=True).count()
        context["total_supplier"] = Supplier.objects.filter(status=True).count()
        context["total_sell"] = SellProduct.objects.all().count()
        context["total_Purchase"] = PurchaseProduct.objects.all().count()
        context["chalans"] = Chalan.objects.filter(status=True)
        return context


class UserManagement(LoginRequiredMixin,
                    UserPassesTestMixin,
                    View):
    def get(self, *args, **kwargs):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(self.request, 'user-management.html', context)
    
    def test_func(self, *args, **kwargs):
        if self.request.user.is_staff:
            return True
        return False


class EditUserManagent(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    UpdateView):
    model = User
    form_class = UserPermissionForm
    template_name = 'edit-user-management.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = 'core:user-management'
    success_message = "Changes saved successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self, *args, **kwargs):
        if self.request.user.is_superuser:
            return True
        return False


class ProductView(LoginRequiredMixin,
                UserPassesTestMixin,
                TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(status=True)
        return context

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

# >>========== DetailView ==============>>

class ChalanDetailView(DetailView):
    model = Chalan
    template_name = 'chalan/chalan_detail.html'

# >=========== create views =============>

class ChalanCreateView(LoginRequiredMixin, 
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        CreateView):
    model = Chalan
    form_class = ChalanCreateForm
    template_name = 'chalan/chalan_create.html'
    success_url = 'core:chalan'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create New Chalan'
        context["chalans"] = Chalan.objects.filter(status=True)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

class ProductCreateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        View):
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
            supplier_price= form.cleaned_data.get('supplier_price')
            sell_price = form.cleaned_data.get('sell_price')
            description = form.cleaned_data.get('description')
            quantity = form.cleaned_data.get('quantity')
            warehouse = form.cleaned_data.get('warehouse')
            office = self.request.user.office
            
            new_dept = Product(category=category,
                            name=name,
                            supplier_price=supplier_price,
                            sell_price=sell_price,
                            description=description,
                            added_by=added_by,
                            quantity=quantity,
                            office=office,
                            warehouse=warehouse)
            new_dept.save()
            messages.success(self.request, 'Product added successfully')
            return redirect('/')
        else:
            messages.warning(self.request, 'Something went wrong')
            return redirect('/')
    
    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class DeparmentCreateView(LoginRequiredMixin, 
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        CreateView):
    model = Department
    template_name = 'department.html'
    form_class = DeptForm
    success_url = 'core:department'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Create new department'
        context["departments"] = Department.objects.filter(status=True)
        return context

    def form_valid(self, form):
        form.instance.office = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class CategoryCreateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        CreateView):
    model = Category
    template_name = 'category.html'
    form_class = CategoryForm
    success_url = 'core:category'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add new category'
        context["categories"] = Category.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class WarehouseCreateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        CreateView):
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

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class BankCreateView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    CreateView):
    model = Bank
    template_name = 'bank.html'
    form_class = BankForm
    success_url = 'core:bank'
    success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banks"] = Bank.objects.filter(status=True)
        context["title"] = 'Add new bank'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class TransactionCreateView(LoginRequiredMixin,
                            UserPassesTestMixin,
                            SuccessMessageMixin,
                            CreateView):
    model = BankTransaction
    template_name = 'transaction.html'
    form_class = BankTransactionForm
    success_url = 'core:transaction'
    success_message = "Transaction was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transactions"] = BankTransaction.objects.filter(status=True)
        context["title"] = 'Add new transaction'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


# >=========== update views =============>


class ChalanUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        UpdateView):
    model = Chalan
    form_class = ChalanCreateForm
    template_name = 'chalan/chalan_create.html'
    success_url = 'core:chalan'
    success_message = "%(name)s was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Chalan'
        context["chalans"] = Chalan.objects.filter(status=True)
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class ProductUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        UpdateView):
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
        if self.request.user.is_staff:
            return True
        return False


class DepartmentUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        UpdateView):
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
        if self.request.user.is_staff:
            return True
        return False


class CategoryUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        UpdateView):
    model = Category
    form_class = CategoryForm
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
        if self.request.user.is_staff:
            return True
        return False


class WarehouseUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        UpdateView):
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

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class BankUpdateView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    UpdateView):
    model = Bank
    template_name = 'bank.html'
    form_class = BankForm
    success_url = 'core:bank'
    success_message = "%(name)s was Updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banks"] = Bank.objects.filter(status=True)
        context["title"] = 'Edit bank'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class TransactionUpdateView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        UpdateView):
    model = BankTransaction
    template_name = 'transaction.html'
    form_class = BankTransactionForm
    success_url = 'core:transaction'
    success_message = "Transaction was Updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transactions"] = BankTransaction.objects.filter(status=True)
        context["title"] = 'Edit transaction'
        return context
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


# >=================== delete views ===============>


class ChalanDeleteView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    DeleteView):
    model = Chalan
    template_name = 'delete.html'
    success_url = 'core:chalan'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = 'core:home'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class DepartmentDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        DeleteView):
    model = Department
    template_name = 'delete.html'
    success_url = 'core:department'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CategoryDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = 'core:home'
    success_message = "%(name)s was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class WarehouseDeleteView(LoginRequiredMixin,
                        UserPassesTestMixin,
                        SuccessMessageMixin,
                        DeleteView):
    model = Warehouse
    template_name = 'delete.html'
    success_url = 'core:home'
    success_message = "%(name)s was deleted successfully"
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class BankDeleteView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    DeleteView):
    model = Bank
    template_name = 'delete.html'
    success_url = 'core:bank'
    success_message = "%(name)s was deleted successfully"
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class TransactionDeleteView(LoginRequiredMixin,
                            UserPassesTestMixin,
                            SuccessMessageMixin,
                            DeleteView):
    model = BankTransaction
    template_name = 'delete.html'
    success_url = 'core:transaction'
    success_message = "%(transaction_type)s was deleted successfully"
    
    def get_success_url(self, **kwargs):
        return reverse(self.success_url)
    
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False
