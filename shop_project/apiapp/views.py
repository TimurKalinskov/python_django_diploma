from django.contrib.auth import login, logout
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Banner, Tag, Category, Product
from orders.models import Order
from . import serializers
from .filtersets import CatalogFilter
from .paginators import CustomPagination
from .serializers import BasketSerializer, BasketBaseSerializer, BannersSerializer, TagSerializer, CategorySerializer, \
    CatalogSerializer, OrderSerializer
from basket.models import Basket


class BasketModelView(viewsets.ModelViewSet):
    queryset = Basket.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            return BasketSerializer
        return BasketBaseSerializer


class BannerModelView(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannersSerializer


class TagModelView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductsModelView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CatalogSerializer
    pagination_class = CustomPagination
    filterset_class = CatalogFilter


class OrdersModelView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        print(request.data)

        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class Categories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)
