from rest_framework import serializers
from .models import *


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        

class OrderSerializer(serializers.ModelSerializer):
    orderitems = serializers.SerializerMethodField(method_name="get_order_items", read_only=True)
    
    def get_order_items(self, obj):
        order_items = obj.orderitems.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data

    class Meta:
        model = Order
        fields = ('id', 'orderitems')
        
        