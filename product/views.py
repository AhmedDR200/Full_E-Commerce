from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from .filters import ProductsFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_all(request):
    filterset = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterset.qs.count()
    res_page = 20
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
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    
    if serializer.is_valid():
        product = Product.objects.create(**data,user=request.user)
        serializer = ProductSerializer(product, many=False)
            
        return Response(
            {
                "status":True,
                "message": "Created Successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK)
    else:
        return Response(
            {
                "status": False,
                "message": "Faild!",
                "errors":serializer.errors
                },
            status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if product.user != request.user:
        return Response({"error":"You don't have permission to edit this product"}, status=status.HTTP_403_FORBIDDEN)
    
    product.name = request.data['name']
    product.description = request.data['description']
    product.price = request.data['price']
    product.brand = request.data['brand']
    product.category = request.data['category']
    product.rate = request.data['rate']
    product.stock = request.data['stock']
    product.save()
    
    serializer = ProductSerializer(product, many=False)
                
    return Response(
            {
                "status": True,
                "message":"Updated successfully",
                "data" : serializer.data 
            },
            status=status.HTTP_201_CREATED)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if product.user != request.user:
        return Response(
            {"error": 'You do not have permission to perform this action.'},
            status=status.HTTP_403_FORBIDDEN
        )
        
    product.delete()
    return Response({"success":True,"message":"Deleted Successfully"},status=status.HTTP_200_OK)