# Generated by Django 3.0.6 on 2020-06-10 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=11)),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=100)),
                ('Product', models.ManyToManyField(to='core.Product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.Customer')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Warehouse')),
            ],
        ),
    ]
