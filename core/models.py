from django.conf import settings
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Office(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    office = models.OneToOneField(Office, on_delete=models.CASCADE, to_field='name', blank=True, null=True)

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
    