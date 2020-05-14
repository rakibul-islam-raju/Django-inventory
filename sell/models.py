from django.db import models
from django.urls import reverse
from core.models import Warehouse


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.DecimalField(decimal_places=0, max_digits=11)
    address = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("sell:customer-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("sell:customer-delete", kwargs={"pk": self.pk})


class SellProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    added_by = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_total_price(self):
        result = self.price * self.quantity
    
    def get_update_url(self):
        return reverse("sell:sell-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("sell:sell-delete", kwargs={"pk": self.pk})