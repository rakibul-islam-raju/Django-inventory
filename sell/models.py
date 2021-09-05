from django.db import models
from django.urls import reverse
from core.models import Product


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    address = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("sell:customer-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("sell:customer-delete", kwargs={"pk": self.pk})


class SellProduct(models.Model):
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(blank=True, null=True)

    added_by = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name

    @property
    def get_total_price(self):
        result = self.price * self.quantity
        return result

    def get_update_url(self):
        return reverse("sell:sell-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("sell:sell-delete", kwargs={"pk": self.pk})
