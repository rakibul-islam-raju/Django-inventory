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
        # fields = '__all__'
        fields = ['name', 'description']


class CategotyForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['category', 'name', 'price', 'quantity', 'description']


class WarehouseForm(forms.ModelForm):

    class Meta:
        model = Warehouse
        fields = '__all__'
