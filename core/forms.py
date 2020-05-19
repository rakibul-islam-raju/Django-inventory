from django import forms
from .models import Office, Department, Category, Product, User, Warehouse, Bank, BankTransaction

from allauth.account.forms import SignupForm


offices = Office.objects.all()
# offices = offices.name

class MyCustomSignupForm(SignupForm):
    office = forms.ModelChoiceField(offices)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.office = self.cleaned_data['office']
        user.save()
        return user


class DeptForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }


class CategotyForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['department', 'name']


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'warehouse', 'name', 'quantity', 'supplier_price', 'sell_price', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }


class WarehouseForm(forms.ModelForm):

    class Meta:
        model = Warehouse
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }


class BankForm(forms.ModelForm):

    class Meta:
        model =Bank
        fields = ['name', 'ac_name', 'ac_number', 'branch']
        labels = {
            'ac_name': 'A/C Name',
            'ac_number': 'A/C Number',
        }


class BankTransactionForm(forms.ModelForm):

    class Meta:
        model = BankTransaction
        fields = ['bank', 'date', 'account_type', 'description', 'transaction_type', 'amount']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
            'date': forms.TextInput(attrs={'type': 'date'})
        }
