from rest_framework import serializers
from models import Cart,ProductGroup,Discount,Product,OrderLine,PriceChange,Store,Storage,StorageChange

class Cart(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class ProductGroup(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'

class Discount(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class Product(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderLine(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = '__all__'

class PriceChange(serializers.ModelSerializer):
    class Meta:
        model = PriceChange
        fields = '__all__'

class Store(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class Storage(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class StorageChange(serializers.ModelSerializer):
    class Meta:
        model = StorageChange
        fields = '__all__'
