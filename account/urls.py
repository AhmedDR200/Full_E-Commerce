from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('user/', current_user,name='user_info'),
    path('user/update/', update_user,name='update_user'),
]
