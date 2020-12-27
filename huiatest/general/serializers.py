from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Client,
    QualityLot,
    Product,
    Order
)

# https://www.django-rest-framework.org/api-guide/serializers/

class ClientSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = ['name', 'cpf', 'birth_date', 'inactive']


class SellerSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'


class QualityLotSerializer(serializers.ModelSerializer):

    class Meta:

        model = QualityLot
        fields = ['id', 'fabrication_date', 'quality', 'inactive']       


class ProductSerializer(serializers.ModelSerializer):    

    class Meta:

        model = Product
        fields = ['name', 'description', 'quality_lot', 'color', 'price', 'inactive']  


class OrderSerializer(serializers.ModelSerializer):
    class Meta:

        model = Order
        fields = ['id', 'client', 'seller', 'products', 'purchase_date', 'total_value', 'inactive']      



class OrderListSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    seller = SellerSerializer()
    products = ProductSerializer(many=True)
    class Meta:

        model = Order
        fields = ['id', 'client', 'seller', 'products', 'purchase_date', 'total_value', 'inactive']  