from django.db import models

# Create your models here.
from django.urls import reverse


# class Category(models.Model):
#     sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True,
#                                      blank=True)
#     is_sub = models.BooleanField(default=False)
#     name = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, unique=True)
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('shop:category_filter', args={self.slug})

class Banner(models.Model):
    filler = models.TextField()


class Tag(models.Model):
    name = models.TextField(max_length=50)


class Image(models.Model):
    image = models.ImageField(upload_to='images', default='D:/skillbox/shop_project/frontend/static/frontend/assets'
                                                          '/img/content/home/bigGoods.png')


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    images = models.ManyToManyField(Image, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    freeDelivery = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', args={self.slug, })
