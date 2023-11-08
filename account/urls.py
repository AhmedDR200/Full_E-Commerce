from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('user/', current_user,name='user_info'),
    path('user/update/', update_user,name='update_user'),
    path('forgot_password/', forget_password, name='forget_password'),
    path('reset_password/<str:token>', reset_password, name='reset_password')
]
