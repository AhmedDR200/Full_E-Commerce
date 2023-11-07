from rest_framework import serializers
from .models import Product, Review
from account.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    reviews = serializers.SerializerMethodField(method_name='get_reviews', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'rate','stock', 'brand', 'created_at', 'category', 'username','reviews')
        
    def get_reviews(self,obj):
        reviews = obj.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data    
        
        

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"