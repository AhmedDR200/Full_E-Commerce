from django.urls import path, include
from .views import *

urlpatterns = [
    path('product/', get_all, name="get_all"),
    path('product/<int:pk>/', get_product, name='get_one'),
]