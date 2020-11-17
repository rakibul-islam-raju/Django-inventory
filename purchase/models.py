from django.db import models
from django.urls import reverse
from core.models import Warehouse, User, Category, Subcategory, Bank

from datetime import date


# class Supplier(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.IntegerField()
#     address = models.TextField()
#     status = models.BooleanField(default=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     def get_update_url(self):
#         return reverse("purchase:supplier-edit", kwargs={"pk": self.pk})
    
#     def get_delete_url(self):
#         return reverse("purchase:supplier-delete", kwargs={"pk": self.pk})


class PurchaseProduct(models.Model):
    PAYMENT_TYPE_CHOICE = (
        ('bank', 'Bank'),
        ('cash', 'Cash')
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(Subcategory, blank=True, null=True, on_delete=models.SET_NULL)
    warehouse = models.ForeignKey(Warehouse, null=True, on_delete=models.SET_NULL)

    product_name = models.CharField(max_length=100, unique=True)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    sell_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICE, max_length=4)
    # if payment method == 'bank':
    bank = models.ForeignKey(Bank, blank=True, null=True, on_delete=models.SET_NULL)
    check_no = models.PositiveIntegerField(blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    # endif
    remark = models.TextField(blank=True, null=True, max_length=254)
    
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    @property
    def purchase_no(self):
        product = str(self.product_name)
        d = date.today()
        d = d.strftime("%d%m%y")
        return (product[:3] + str(self.id) + '-' + d).upper()
    
    @property
    def total_cost_price(self):
        return self.cost_price * self.quantity
    
    @property
    def total_sell_price(self):
        return self.sell_price * self.quantity

    def get_update_url(self):
        return reverse("purchase:purchase-edit", kwargs={"pk": self.pk})
    
    def get_delete_url(self):
        return reverse("purchase:purchase-delete", kwargs={"pk": self.pk})
    
    def get_invoice_url(self):
        return reverse("purchase:purchase-invoice", kwargs={"pk": self.pk})

