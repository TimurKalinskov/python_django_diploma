# Generated by Django 4.2.6 on 2023-11-18 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0003_image_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('delivery_type', models.CharField(default='paid', max_length=10)),
                ('payment_type', models.CharField(default='online', max_length=10)),
                ('total_cost', models.FloatField()),
                ('status', models.CharField(default='declined', max_length=10)),
                ('city', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=200)),
                ('products', models.ManyToManyField(to='catalog.product')),
            ],
        ),
    ]
