from django import forms
from .models import Office, Department, Category, Product, User, Warehouse

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
