# Generated by Django 3.0.7 on 2021-09-08 16:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_auto_20210906_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
