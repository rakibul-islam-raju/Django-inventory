# Generated by Django 3.0.7 on 2021-09-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0005_sell_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sellproductitem',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
