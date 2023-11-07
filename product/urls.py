from django.urls import path, include
from .views import *

urlpatterns = [
    path('product/', get_all, name="get_all"),
    path('product/<int:pk>/', get_product, name='get_one'),
    path('update/<int:pk>/', update_product, name='update'),
    path('new/', new_product, name='new_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
    path('<int:pk>/reviews/', add_review, name='add_review')
]