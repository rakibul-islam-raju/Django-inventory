# Generated by Django 3.0.6 on 2020-10-03 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201002_1710'),
        ('sell', '0007_auto_20200927_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellproduct',
            name='chalan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Chalan'),
        ),
    ]