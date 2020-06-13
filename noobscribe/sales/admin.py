from django.contrib import admin
from django.utils import translation
from .forms import OrderProductFormset
from .models import (
    SalesQuotationTemplate,
    SalesQuotation, QuotationExtraFee, QuotationProduct,
    SalesOrder, OrderExtraFee, OrderProduct
)

_ = translation.ugettext_lazy


class QuotationExtraFeeLine(admin.TabularInline):
    extra = 0
    min_num = 1
    model = QuotationExtraFee
    raw_id_fields = ['fee']


class QuotationProductLine(admin.TabularInline):
    extra = 0
    min_num = 1
    model = QuotationProduct
    raw_id_fields = ['product']


class OrderExtraFeeLine(admin.TabularInline):
    extra = 0
    min_num = 1
    model = OrderExtraFee
    raw_id_fields = ['fee']


class OrderProductLine(admin.TabularInline):
    extra = 0
    min_num = 1
    model = OrderProduct
    formset = OrderProductFormset
    raw_id_fields = ['product']


@admin.register(SalesQuotationTemplate)
class QuotationTemplateAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'body']


@admin.register(SalesOrder)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderExtraFeeLine, OrderProductLine]
    date_hierarchy = 'created_at'
    search_fields = ['inner_id', 'customer']
    list_display = [
            'inner_id',
            'customer',
            'created_at',
            'total_order',
            'discount',
            'grand_total',
            'status'
        ]
    list_select_related = ['customer']
    raw_id_fields = ['customer']
    actions = ['trash_action', 'draft_action', 'validate_action']

    def state(self, obj):
        return obj.get_status_display()

    def trash_action(self, request, queryset):
        try:
            for i in queryset.all():
                i.trash()
        except PermissionError as err:
            print(err)

    trash_action.short_description = _('Trash selected Sales Orders')

    def draft_action(self, request, queryset):
        try:
            for i in queryset.all():
                i.draft()
        except PermissionError as err:
            print(err)

    draft_action.short_description = _('Draft selected Sales Orders')

    def validate_action(self, request, queryset):
        try:
            for i in queryset.all():
                i.validate()
        except PermissionError as err:
            print(err)

    validate_action.short_description = _('Validate selected Sales Orders')


@admin.register(SalesQuotation)
class QuotationAdmin(admin.ModelAdmin):
    inlines = [QuotationExtraFeeLine, QuotationProductLine]
    date_hierarchy = 'created_at'
    search_fields = ['inner_id', 'customer']
    list_display = [
            'inner_id',
            'customer',
            'created_at',
            'total_amount',
            'discount',
            'grand_total'
        ]
    list_select_related = ['customer']
    raw_id_fields = ['customer']
