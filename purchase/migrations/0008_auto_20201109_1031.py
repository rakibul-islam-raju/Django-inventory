# Generated by Django 3.0.7 on 2020-11-09 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20201109_0935'),
        ('purchase', '0007_purchaseproduct_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseproduct',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Subcategory'),
        ),
    ]
