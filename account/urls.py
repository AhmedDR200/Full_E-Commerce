from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register, name="register"),
    path('user/', current_user,name='user_info'),
]
