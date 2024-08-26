from django.contrib import admin

from basket.models import Basket, OrderItem


# Register your models here.
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class BasketAdmin(admin.ModelAdmin):
    pass
