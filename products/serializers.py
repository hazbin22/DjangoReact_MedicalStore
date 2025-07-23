from rest_framework import serializers
from .models import Product, Company

class ProductSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'stock', 'available', 'company']

class ProductDetailSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'