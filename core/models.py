from django.conf import settings
from django.db import models
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from datetime import date
import barcode
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Office(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, to_field='name', blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    def __str__(self):
        return str(self.office)


class Department(models.Model):
    office = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True) 
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("core:department-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:department-delete", kwargs={"pk": self.pk})
    

class Category(models.Model):
    department = models.ForeignKey(Department, models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("core:category-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:category-delete", kwargs={"pk": self.pk})


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("core:warehouse-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:warehouse-delete", kwargs={"pk": self.pk})


class Product(models.Model):
    category = models.ForeignKey(Category, models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, models.CASCADE, related_name='inventory_product')
    office = models.ForeignKey(User, models.CASCADE)

    name = models.CharField(max_length=100, unique=True)
    qr_code = models.ImageField(upload_to='qrcodes', blank=True, null=True)
    supplier_price = models.FloatField()
    sell_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    added_by = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_profit_per_product(self):
        if self.sell_price > self.supplier_price:
            profit = self.sell_price - self.supplier_price
            result = (profit / self.supplier_price) * 100
            result = round(result, 2)
            return result
    
    def get_loss_per_product(self):
        if self.sell_price < self.supplier_price:
            loss = self.supplier_price - self.sell_price
            result = (loss / self.supplier_price) * 100
            result = round(result, 2)
            return result

    def get_update_url(self):
        return reverse("core:product-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:product-delete", kwargs={"pk": self.pk})

    def get_unique_number(self):
        cat = str(self.category.name)
        ware = str(self.warehouse.name)
        name = str(self.name)
        _id = str(self.id)
        d = date.today()
        d = d.strftime("%d%m%y")

        unique_number = cat[0] + ware[0] + name[0] + _id + '-' + d
        unique_number = unique_number.upper()

        return unique_number

    

class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ac_name = models.CharField(max_length=100)
    ac_number = models.DecimalField(decimal_places=0, max_digits=20)
    branch = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse("core:bank-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:bank-delete", kwargs={"pk": self.pk})
    

account_type_choices = (
    ('C', 'Credit'),
    ('D', 'Debit')
)

transaction_type_choices = (
    ('W', 'Withdraw'),
    ('D', 'Deposite')
)

class BankTransaction(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    date = models.DateField()
    account_type = models.CharField(choices=account_type_choices, max_length=1)
    description = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(max_length=1, choices=transaction_type_choices)
    amount = models.FloatField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.account_type
    
    def get_update_url(self):
        return reverse("core:transaction-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("core:transaction-delete", kwargs={"pk": self.pk})