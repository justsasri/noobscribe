import uuid
from django.db import models
from django.utils import translation, timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

from django_numerators.models import NumeratorMixin
from django_qrcodes.models import QRCodeMixin

from ...plans.models import Product, Quota, Membership
# from ...core.mixins import ThreeStepStatusMixin
from .managers import SalesOrderManager, CartManager
# from .mixins import InvoiceStatusMixin


_ = translation.gettext_lazy



class Cart(models.Model):
    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    objects = CartManager()

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid'
    )
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.PROTECT,
        related_name='carts',
        verbose_name=_('Owner'))
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='cart_items')
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name=_('Quantity'),
        validators=[
            MinValueValidator(1, message=_('Minimal value: 1')),
            MaxValueValidator(100, message=_('Maximal value: 500'))
        ])

    def __str__(self):
        return self.product.name


class SalesOrder(QRCodeMixin, NumeratorMixin, models.Model):
    class Meta:
        verbose_name = _('Sales Order')
        verbose_name_plural = _('Sales Orders')
        permissions = (
            ('draft_salesorder', _('Can draft Sales Order')),
            ('trash_salesorder', 'Can trash Sales Order'),
            ('validate_salesorder', 'Can validate Sales Order'),
            ('complete_salesorder', 'Can complete Sales Order'),
        )

    objects = SalesOrderManager()

    doc_prefix = 'SO'

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid'
    )
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('Owner'))
    promo_code = models.CharField(
        max_length=32,
        null=True, blank=True,
        verbose_name=_('Promo Code'))
    note = models.CharField(
        max_length=244,
        null=True, blank=True,
        verbose_name=_("Note"))
    discount_percentage = models.DecimalField(
        default=0, 
        max_digits=15,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ], verbose_name=_('Discount'),
        help_text=_('Discount in percent'))
    discount = models.DecimalField(
        default=0, 
        max_digits=15,
        decimal_places=2,
        verbose_name=_('Total discount'))
    total_order = models.DecimalField(
        default=0, max_digits=15,
        decimal_places=2,
        verbose_name=_('Total Order'))

    def __str__(self):
        return "{} ({})".format(self.inner_id, self.owner)

    def calc_total_order(self):
        # FakeQuerySet doesn't have aggregate
        total_plans = self.order_items.aggregate(
                val=models.Sum('total_price')
            )['val'] or 0
        self.total_order = total_plans
        return self.total_order

    def calc_total_discount(self):
        self.discount = ((self.total_order * self.discount_percentage) / 100)

    def calc_grand_total(self):
        self.grand_total = self.total_order - self.discount

    def calc_all_total(self):
        self.calc_total_order()
        self.calc_total_discount()
        self.calc_grand_total()

    def save(self, *args, **kwargs):
        self.is_specific = True  # Grouping Product
        self.calc_all_total()
        self.clean()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')
        ordering = ('product',)
        unique_together = ('order', 'product')
    
    _ori_product = None

    order = models.ForeignKey(
        SalesOrder,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name=_('Order'))
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='order_items')
    unit_price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        verbose_name=_('unit price'))
    quantity = models.PositiveIntegerField(
        default=1, verbose_name=_('Quantity'),
        validators=[
            MinValueValidator(1, message=_('Minimal value: 1')),
            MaxValueValidator(500, message=_('Maximal value: 500'))
        ])
    total_price = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        verbose_name=_('Total Price'))
    note = models.CharField(
        null=True, blank=True,
        max_length=244,
        verbose_name=_('Note'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if getattr(self, 'product', False):
            self._ori_product = self.product

    def __str__(self):
        return self.product.name

    def clean(self):
        # Make sure product type equal to sales order type
        # if self.order != self.product.product_type:
        #     msg = _("Sales order doesn't match.")
        #     raise ValidationError({"order": msg})
        # Make sure price don't change directly when tarif price changed
        not_adding = self._state.adding is False
        if self._ori_product:
            is_changed = self._ori_product.id != self.product.id
        else:
            is_changed = False
        if not_adding and is_changed:
            msg = _("Product can't be changed, please delete instead.")
            raise ValidationError({"product": msg})
        super().clean()

    def save(self, *args, **kwargs):
        product = self.product.get_real_instance()
        self.unit_price = product.price
        self.total_price = self.unit_price * self.quantity
        self.clean()
        super().save(*args, **kwargs)


# class Invoice(QRCodeMixin, NumeratorMixin, InvoiceStatusMixin, BaseModel):
#     class Meta:
#         verbose_name = _('Invoice')
#         verbose_name_plural = _('Invoices')

#     sales_order = models.OneToOneField(
#         SalesOrder,
#         on_delete=models.PROTECT,
#         verbose_name=_('sales order'))
#     due_date = models.DateTimeField(
#         default=timezone.now, verbose_name=_('Due date'))
#     description = models.TextField(
#         max_length=MaxLength.TEXT,
#         blank=True, null=True, verbose_name=_('Description'))
#     total_order = models.DecimalField(
#         default=0, max_digits=15,
#         decimal_places=2,
#         verbose_name=_('Total Order'))
#     discount_percentage = models.DecimalField(
#         default=0, max_digits=15,
#         decimal_places=2,
#         validators=[
#             MinValueValidator(0),
#             MaxValueValidator(100)
#         ], verbose_name=_('Discount'),
#         help_text=_('Discount in percent'))
#     discount = models.DecimalField(
#         default=0, max_digits=15,
#         decimal_places=2,
#         verbose_name=_('Total discount'))
#     grand_total = models.DecimalField(
#         default=0,
#         max_digits=15,
#         decimal_places=2,
#         verbose_name=_('Grand Total'))
#     downpayment = models.DecimalField(
#         default=0,
#         max_digits=15,
#         decimal_places=2,
#         verbose_name=_('down payment'))
#     repayment = models.DecimalField(
#         default=0,
#         max_digits=15,
#         decimal_places=2,
#         verbose_name=_('repayment'))
#     paid = models.DecimalField(
#         default=0,
#         max_digits=15,
#         decimal_places=2,
#         verbose_name=_('paid'))
#     receivable = models.DecimalField(
#         default=0,
#         max_digits=15,
#         decimal_places=2,
#         verbose_name=_('receivable'))
#     refund = models.DecimalField(
#         default=0,
#         max_digits=15,
#         decimal_places=2,
#         verbose_name=_('refund'))

#     @property
#     def is_payment_complete(self):
#         return self.grand_total == self.paid

#     @property
#     def close_ignore_condition(self):
#         return self.is_closed

#     @property
#     def close_valid_condition(self):
#         return self.is_paid and self.grand_total == self.paid
