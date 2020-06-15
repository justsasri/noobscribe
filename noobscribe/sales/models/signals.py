from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .orders import OrderItem


@receiver(post_save, sender=OrderItem)
def after_save_order_item(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    instance.order.save()


@receiver(post_delete, sender=OrderItem)
def after_delete_order_item(sender, **kwargs):
    instance = kwargs.pop('instance', None)
    instance.order.save()
