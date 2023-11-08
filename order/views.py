from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response(
        {
            'status': 200,
            'message':'success',
            'data': serializer.data
            },
        status=status.HTTP_200_OK
    )



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request,pk):
    order =get_object_or_404(Order, id=pk)

    serializer = OrderSerializer(order,many=False)
    return Response(
        {
            'status': True,
            'message':'success',
            'data': serializer.data
            },
        status=status.HTTP_200_OK
    )



@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def process_order(request,pk):
    order =get_object_or_404(Order, id=pk)
    order.status = request.data['status']
    order.save()
     
    serializer = OrderSerializer(order,many=False)
    return Response(
        {
            'status': True,
            'message':'Updated Successfully',
            'data': serializer.data
            },
        status=status.HTTP_201_CREATED
    )



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request,pk):
    order =get_object_or_404(Order, id=pk) 
    order.delete()
      
    return Response(
        {
            'status': True,
            'message':'Deleted Successfully'
            },
        status=status.HTTP_204_NO_CONTENT
    )



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user = request.user 
    data = request.data
    order_items = data['order_Items']

    if order_items and len(order_items) == 0:
       return Response({'error': 'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
    else:
        total_amount = sum( item['price']* item['quantity'] for item in order_items)
        order = Order.objects.create(
            user = user,
            city = data['city'],
            zip_code = data['zip_code'],
            phone = data['phone'],
            address = data['address'],
            total_amount = total_amount,
        )
        for i in order_items:
            product = Product.objects.get(id=i['product'])
            item = OrderItem.objects.create(
                product= product,
                order = order,
                name = product.name,
                quantity = i['quantity'],
                price = i['price']
            )
            product.stock -= item.quantity
            product.save()
        serializer = OrderSerializer(order,many=False)
        return Response(
            {
                'status': True,
                'message':'Successfully created a new order',
                'data':serializer.data
            },
            status=status.HTTP_201_CREATED
        )