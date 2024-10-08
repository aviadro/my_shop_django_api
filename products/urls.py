
from django.contrib import admin
from django.urls import include, path

from products import views

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('<int:id>/', views.product_detail, name="product_detail"),
    path('categories/', views.category_list, name="category_list"),
    path('cart/', views.get_cart_products, name='get_cart_products'),

]
