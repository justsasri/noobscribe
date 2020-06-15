from django.contrib import admin
from .models import (
    Product,
    Quota,
    Membership
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'unit_of_measure',
        'price',
    ]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'unit_of_measure',
        'validity',
        'price',
    ]


@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_filter = [
        'platform',
        'balance_type'
    ]
    list_display = [
        'name',
        'platform',
        'balance_type',
        'quantity',
        'price',
    ]