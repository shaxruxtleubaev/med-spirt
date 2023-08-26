from django.urls import path, include
from .views import (
    client_list,
    blog_list,
    sponsor_list,
    product_list,
)

urlpatterns = [
    path('clients/', client_list, name='client-list'),
    path('blogs/', blog_list, name='blog-list'),
    path('sponsors/', sponsor_list, name='sponsor-list'),
    path('products/', product_list, name='product-list')
]