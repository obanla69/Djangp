from decimal import Decimal

from rest_framework import serializers

from store.models import Collection, Products, Review, Cart, CartItem


class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    class Meta:
        model = Collection
        fields = ['id', 'title']


class CreateCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    # collection = CreateCollectionSerializer()
    class Meta:
        model = Products
        fields = ['title', 'price', 'description', 'Inventory', 'collection']


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'price', 'description', 'Inventory', 'collection']

    # collection = serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail'
    # )
    discount = serializers.SerializerMethodField(method_name='discount_price')

    class Meta:
        model = Products
        fields = ['id', 'title', 'price', 'Inventory', 'discount', 'collection']

    def discount_price(self, products: Products):
        return products.price * Decimal(0.10)

    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # Inventory = serializers.IntegerField()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "customer", "product", "title", "content"]


class CartItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title', 'description', 'price']


#
class CartItemSerializer(serializers.ModelSerializer):
    product = CartItemProductSerializer()
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price'
    )

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.price * cart_item.quantity


class CartSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(
        method_name='get_total_price'
    )

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def get_total_price(self, cart: Cart):
        return sum([item.quantity * item.product.price for item in cart.items.all()])
