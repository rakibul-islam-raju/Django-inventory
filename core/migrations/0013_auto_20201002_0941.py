# Generated by Django 3.0.6 on 2020-10-02 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201002_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chalan_out',
            name='product',
        ),
        migrations.DeleteModel(
            name='Chalan_In',
        ),
        migrations.DeleteModel(
            name='Chalan_Out',
        ),
    ]
