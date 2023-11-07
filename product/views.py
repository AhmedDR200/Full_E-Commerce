from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from .filters import ProductsFilter
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_all(request):
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    res_page = 2
    paginator = PageNumberPagination()
    paginator.page_size = res_page
    queryset = paginator.paginate_queryset(filterset.qs, request)
    # products = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(
        {
            "status":True,
            "message": "Done!",
            "data": serializer.data,
            "products count": count,
            "per page": res_page,
        },
        status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_product(request, pk):
    products = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(
        {
            "status":True,
            "message": "Done!",
            "data": serializer.data
        },
        status=status.HTTP_200_OK) 