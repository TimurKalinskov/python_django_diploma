from django.contrib.auth.models import User
from django.db import models


class OrderItem(models.Model):
    image_number = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    image_size = models.CharField(max_length=50)
    file_type = models.CharField(max_length=20)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.user)
#

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    count = models.IntegerField()
    # category = models.ForeignKey("""Category""", on_delete=models.CASCADE)
    # price = models.FloatField()
    # count = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)
    # "title": "video card",
    # "description": "description of the product",
    # "freeDelivery": true,
    # "images": [
    #     {
    #         "src": "/3.png",
    #         "alt": "Image alt string"
    #     }
    # ],
    # "tags": [
    #     {
    #         "id": 12,
    #         "name": "Gaming"
    #     }
    # ],
    # "reviews": 5,
    # "rating":
