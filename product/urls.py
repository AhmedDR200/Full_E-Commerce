from django.urls import path, include
from .views import *

urlpatterns = [
    path('product/', get_all, name="get_all"),
]