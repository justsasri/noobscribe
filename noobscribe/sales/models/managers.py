from django.db import models


class CartManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def user_cart(self, request):
        cart_items = self.filter(owner=request.user)
        return cart_items

    def add_product(self, request, product):
        from .orders import Cart
        defaults = {
            'owner': request.user,
            'product': product
        }
        product, created = self.get_or_create(**defaults, defaults=defaults)
        return product


class SalesOrderManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs
