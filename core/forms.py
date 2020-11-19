from django import forms
from .models import *

from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=14,
                            min_length=11,
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
                        )

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        phone = self.cleaned_data['phone']
        user.phone = phone
        user.save()
        return user


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }


class SubcategoryForm(forms.ModelForm):

    class Meta:
        model = Subcategory
        fields = ['category', 'name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': '2'}),
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category',
                'subcategory',
                'warehouse',
                'product_name',
                'quantity',
                'sell_price',
                'description']
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

class UserPermissionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',
                'email',
                'first_name',
                'last_name',
                'organization',
                'is_active',
                'is_staff',]


# class ChalanCreateForm(forms.ModelForm):

#     class Meta:
#         model = Chalan
#         fields = ['name', 'description']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': '2'}),
#         }