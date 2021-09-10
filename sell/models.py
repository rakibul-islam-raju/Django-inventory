import datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from core.models import Product, User


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11)

    status = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_update_url(self):
        return reverse("sell:customer-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("sell:customer-delete", kwargs={"pk": self.pk})


class Sell(models.Model):
    customer = models.ForeignKey(
        Customer, blank=True, null=True, on_delete=models.SET_NULL)
    invoice_number = models.CharField(max_length=50, blank=True)

    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number

    def save(self, *args, **kwargs):
        today = datetime.date.today()
        today_string = today.strftime('%y%m%d')
        next_invoice_number = '01'
        last_invoice = Sell.objects.filter(
            invoice_number__startswith=today_string).order_by('invoice_number').last()
        if last_invoice:
            last_invoice_number = int(last_invoice.invoice_number[6:])
            next_invoice_number = '{0:02d}'.format(last_invoice_number + 1)
        self.invoice_number = today_string + next_invoice_number
        super(Sell, self).save(*args, **kwargs)

    @property
    def total_price(self):
        return sum(item.get_total_price for item in self.sellproductitem_set.all())

    def get_update_url(self):
        return reverse("sell:sale-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("sell:sale-delete", kwargs={"pk": self.pk})


class SellProductItem(models.Model):
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(decimal_places=2, max_digits=8)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_name

    @property
    def get_total_price(self):
        return self.price * self.quantity

    def get_update_url(self):
        return reverse("sell:sell-edit", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("sell:sell-delete", kwargs={"pk": self.pk})
