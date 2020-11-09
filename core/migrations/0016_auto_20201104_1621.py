# Generated by Django 3.0.6 on 2020-11-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20201002_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chalan',
            name='name',
            field=models.CharField(help_text='Example: ABC-01122020', max_length=254, unique=True),
        ),
    ]