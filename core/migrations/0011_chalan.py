# Generated by Django 3.0.6 on 2020-10-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200928_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chalan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chalan_name', models.CharField(max_length=254)),
                ('chalan_type', models.CharField(choices=[('in', 'in'), ('out', 'out')], max_length=3)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('product', models.ManyToManyField(to='core.Product')),
            ],
        ),
    ]
