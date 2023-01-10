from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('shop/', views.shop, name='shop'),
    path('detail/', views.details, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.checkout, name='contact'),
    path('addToCart/', views.addToCart, name='addToCart'),
]
