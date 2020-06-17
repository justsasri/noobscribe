from django.urls import path
from .views import (
    ProductIndexView,
    CartView,
    CheckoutView,
    cart_add_product,
    cart_remove_product
)

urlpatterns = [
    path('', ProductIndexView.as_view(), name='shop_index'),
    path('checkout/', CheckoutView.as_view(), name='cart_checkout'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/', cart_add_product, name='cart_add_product'),
    path('cart/delete/', cart_remove_product, name='cart_remove_product')
    
]