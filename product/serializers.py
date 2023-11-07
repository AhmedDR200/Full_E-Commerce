from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'rate','stock', 'brand', 'created_at', 'category', 'username',)
        