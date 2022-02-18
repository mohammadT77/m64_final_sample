from django.urls import path
from .apis import *

urlpatterns = [
    path('list/', ProductListAPI.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailAPI.as_view(), name=''),
]
