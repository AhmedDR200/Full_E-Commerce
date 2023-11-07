import django_filters
from .models import *

class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name="name", lookup_expr="icontains")
    max_price = django_filters.filters.NumberFilter(field_name="price" or 0, lookup_expr="gte")
    min_price = django_filters.filters.NumberFilter(field_name="price" or 100000, lookup_expr="lte")
    
    class Meta:
        model = Product
        fields = ('category', 'brand','keyword','max_price', 'min_price')
        