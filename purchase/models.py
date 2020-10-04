from django.db import models
from django.urls import reverse
from core.models import Warehouse, User, Category, Chalan


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("purchase:supplier-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("purchase:supplier-delete", kwargs={"pk": self.pk})


class PurchaseProduct(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
    chalan = models.ForeignKey(Chalan, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    
    added_by = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_total_price(self):
        result = self.price * self.quantity
        return result

    def get_update_url(self):
        return reverse("purchase:purchase-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("purchase:purchase-delete", kwargs={"pk": self.pk})

