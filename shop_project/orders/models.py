from django.core.validators import RegexValidator
from django.db import models
from catalog.models import Product


# Create your models here.
class Order(models.Model):
    products = models.ManyToManyField(Product)
    createdAt = models.DateTimeField(auto_now_add=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    deliveryType = models.CharField(max_length=10, default='paid')
    paymentType = models.CharField(max_length=10, default='online')
    totalCost = models.FloatField()
    status = models.CharField(max_length=10, default='declined')
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=200)


