# Generated by Django 3.0.7 on 2021-09-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0004_auto_20210908_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]