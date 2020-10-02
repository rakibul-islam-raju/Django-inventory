from django.db import models
from core.models import Product

class Chalan_In(models.Model):
    chalan_name = models.CharField(max_length=254)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(max_length=254)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Chalan In'

    def chalan_total_cost(self):
        return (self.price * self.quantity)

    def __str__(self):
        return self.chalan_name

    # def get_update_url(self):
    #     return reverse("core:department-edit", kwargs={"pk": self.pk})

    # def get_delete_url(self):
    #     return reverse("core:department-delete", kwargs={"pk": self.pk})


class Chalan_Out(models.Model):
    chalan = models.ForeignKey(Chalan_In, on_delete=models.CASCADE)
    chalan_name = models.CharField(max_length=254)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    description = models.TextField(max_length=254)

    class Meta:
        verbose_name_plural = 'Chalan Out'

    def chalan_total_cost(self):
        return (self.price * self.quantity)

    def __str__(self):
        return self.chalan_name
