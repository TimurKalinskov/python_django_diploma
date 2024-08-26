from pip._internal.locations import get_src_prefix

from basket.models import Basket
from catalog.models import Banner, Tag, Category, Product, Image
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

from rest_framework import serializers

from orders.models import Order


class BasketBaseSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = '__all__'

    def get_count(self, obj):
        return '5'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('item', 'count')

    def create(self, validated_data):
        user = self.context.get('request').user
        basket = Basket.objects.create(user=user, **validated_data)
        return basket


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('filler',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', ]


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.get_or_create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField(method_name='get_src')
    alt = serializers.SerializerMethodField(method_name='get_alt')

    class Meta:
        model = Image
        fields = ['src', 'alt']

    def get_src(self, obj):
        if obj.image:
            return obj.image.url

    def get_alt(self, obj):
        if obj.image:
            print(obj.image.url)
            return obj.image.url.split('/')[-1]


class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'subcategories']

    def get_subcategories(self, obj):
        return


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)
    count = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id',
                  'category',
                  'price',
                  'count',
                  'date',
                  'title',
                  'description',
                  'freeDelivery',
                  'images',
                  'tags',
                  'reviews',
                  'rating',
                  ]

    def get_reviews(self, obj):
        return

    def get_rating(self, obj):
        return

    def get_count(self, obj):
        return 1
