from django import forms
from .models import Department, Category, Product, User

from allauth.account.forms import SignupForm


OFFICE_CHOICES = (
    ('Head Office', 'Head Office'),
    ('Uttara Branch', 'Uttara Branch'),
    ('Mirpur Branch', 'Mirpur Branch'),
)


class MyCustomSignupForm(SignupForm):
    office = forms.ChoiceField(choices=OFFICE_CHOICES)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.office = self.cleaned_data['office']
        user.save()
        return user



class DeptForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'
        # fields = ['name', 'description']


class CategotyForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['category', 'name', 'price', 'description']
