from django.db import models
from operator import mod
from django.contrib.auth.models import User
from product.models import Product


class OrderStatus(models.TextChoices):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    CANCELED = 'Canceled'


class PaymentStatus(models.TextChoices):
    UNPAID = 'Unpaid'
    PAYMENT_RECEIVED = 'Payment Received'
    REFUNDED = 'Refunded'
    CHARGEBACK = 'Chargeback'
    APPROVED = 'Approved'
    DENIED = 'Denied'


class PaymentMode(models.TextChoices):
    COD = "COD"
    ONLINE = "Online"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    payment_mode = models.CharField(max_length=15, choices=PaymentMode.choices, default=PaymentMode.COD, blank=False)
    payment_status = models.CharField(max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID, blank=False)
    total_amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=150, default='', blank=False)
    address = models.TextField(max_length=400)
    phone = models.IntegerField(default=0)
    zip_code = models.CharField(max_length=50, default="", blank=False)
    

    def __str__(self):
        return f"{self.user} - {self.order_status}"



class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE, related_name="orderitems")
    name = models.CharField(max_length=150, default="", blank=False)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.FloatField(blank=False, default=0)
    
    def __str__(self):
        return self.name
    