from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
]

handler404 = 'utils.error_view.handler404'
handler500 = 'utils.error_view.handler500'
