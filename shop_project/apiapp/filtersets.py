import django_filters

from catalog.models import Product


class CatalogFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='price__gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='price__lt')
    name = django_filters.CharFilter(field_name='name',  lookup_expr='icontains')
    freeDelivery = django_filters.BooleanFilter(field_name='free_delivery_status', lookup_expr='False')
    available = django_filters.BooleanFilter(field_name='status', lookup_expr='True')

    class Meta:
        model = Product
        fields = ['title', 'price', 'freeDelivery', 'status']
