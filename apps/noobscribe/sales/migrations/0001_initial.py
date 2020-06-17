# Generated by Django 3.0.7 on 2020-06-16 19:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noobscribe_plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('reg_number', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Reg number')),
                ('inner_id', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True, verbose_name='Inner ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('qrcode', models.ImageField(blank=True, editable=False, null=True, upload_to='qrcode')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('promo_code', models.CharField(blank=True, max_length=32, null=True, verbose_name='Promo Code')),
                ('note', models.CharField(blank=True, max_length=244, null=True, verbose_name='Note')),
                ('discount_percentage', models.DecimalField(decimal_places=2, default=0, help_text='Discount in percent', max_digits=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total discount')),
                ('total_order', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Order')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Sales Order',
                'verbose_name_plural': 'Sales Orders',
                'permissions': (('draft_salesorder', 'Can draft Sales Order'), ('trash_salesorder', 'Can trash Sales Order'), ('validate_salesorder', 'Can validate Sales Order'), ('complete_salesorder', 'Can complete Sales Order')),
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Minimal value: 1'), django.core.validators.MaxValueValidator(100, message='Maximal value: 500')], verbose_name='Quantity')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carts', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_items', to='noobscribe_plans.Product')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='unit price')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Minimal value: 1'), django.core.validators.MaxValueValidator(500, message='Maximal value: 500')], verbose_name='Quantity')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=15, verbose_name='Total Price')),
                ('note', models.CharField(blank=True, max_length=244, null=True, verbose_name='Note')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='noobscribe_sales.SalesOrder', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='noobscribe_plans.Product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Order Items',
                'ordering': ('product',),
                'unique_together': {('order', 'product')},
            },
        ),
    ]