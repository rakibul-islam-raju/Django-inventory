from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseProduct
from core.models import Product


@receiver(post_save, sender=PurchaseProduct)
def create_product(sender, instance, created, **kwargs):
    if created:
        Product.objects.create(
            warehouse=instance.warehouse,
            category=instance.category,
            subcategory=instance.sub_category,
            product_name=instance.product_name,
            sell_price=instance.sell_price,
            quantity=instance.quantity,
        )
