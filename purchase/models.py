from django.db import models
from django.urls import reverse
from core.models import Product, User, Bank

from datetime import date


class PurchaseProduct(models.Model):
    PAYMENT_TYPE_CHOICE = (
        ('bank', 'Bank'),
        ('cash', 'Cash')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICE, max_length=4)
    bank = models.ForeignKey(
        Bank, blank=True, null=True, on_delete=models.SET_NULL)
    check_no = models.PositiveIntegerField(blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True, max_length=254)

    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

    @property
    def purchase_no(self):
        product = str(self.product.product_name)
        d = date.today()
        d = d.strftime("%d%m%y")
        return (product[:3] + str(self.id) + '-' + d).upper()

    @property
    def total_price(self):
        return self.price * self.quantity

    def get_update_url(self):
        return reverse("purchase:purchase-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("purchase:purchase-delete", kwargs={"pk": self.pk})

    def get_invoice_url(self):
        return reverse("purchase:purchase-invoice", kwargs={"pk": self.pk})
