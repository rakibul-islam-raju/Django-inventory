from django.conf import settings
from django.db import models
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    address = models.TextField()
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, to_field='name', blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    phone = models.CharField(max_length=11)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
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
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, max_length=100)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("core:category-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:category-delete", kwargs={"pk": self.pk})


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True, max_length=100)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("core:subcategory-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:subcategory-delete", kwargs={"pk": self.pk})


class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("core:warehouse-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:warehouse-delete", kwargs={"pk": self.pk})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='inventory_product')

    product_name = models.CharField(max_length=100)
    cost_price = models.DecimalField(
        default=0, max_digits=8, decimal_places=2, blank=True, null=True)
    sell_price = models.DecimalField(
        default=0, max_digits=8, decimal_places=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_update_url(self):
        return reverse("core:product-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:product-delete", kwargs={"pk": self.pk})

    @property
    def get_unique_number(self):
        cat = str(self.category.name)
        ware = str(self.warehouse.name)
        product_name = str(self.product_name)
        _id = str(self.id)
        d = date.today()
        d = d.strftime("%d%m%y")

        unique_number = cat[0] + ware[0] + product_name[0] + _id + '-' + d
        unique_number = unique_number.upper()

        return unique_number


class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ac_name = models.CharField(max_length=100)
    ac_number = models.DecimalField(decimal_places=0, max_digits=20)
    branch = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("core:bank-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:bank-delete", kwargs={"pk": self.pk})


class BankTransaction(models.Model):
    account_type_choices = (
        ('C', 'Credit'),
        ('D', 'Debit')
    )

    transaction_type_choices = (
        ('W', 'Withdraw'),
        ('D', 'Deposite')
    )

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    date = models.DateField()
    account_type = models.CharField(choices=account_type_choices, max_length=1)
    description = models.TextField(blank=True, null=True)
    transaction_type = models.CharField(
        max_length=1, choices=transaction_type_choices)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_type

    def get_update_url(self):
        return reverse("core:transaction-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("core:transaction-delete", kwargs={"pk": self.pk})
