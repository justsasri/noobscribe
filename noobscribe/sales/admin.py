from django.contrib import admin
from django.utils import translation
from .models import (
    SalesOrder, OrderItem
)

_ = translation.ugettext_lazy


class OrderItemInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(SalesOrder)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    search_fields = ['inner_id', 'customer']
    raw_id_fields = ['owner']
    list_display = [
            'inner_id',
            'created_at',
            'owner',
            'promo_code',
            'total_order'
        ]

#     def state(self, obj):
#         return obj.get_status_display()

#     def trash_action(self, request, queryset):
#         try:
#             for i in queryset.all():
#                 i.trash()
#         except PermissionError as err:
#             print(err)

#     trash_action.short_description = _('Trash selected Sales Orders')

#     def draft_action(self, request, queryset):
#         try:
#             for i in queryset.all():
#                 i.draft()
#         except PermissionError as err:
#             print(err)

#     draft_action.short_description = _('Draft selected Sales Orders')

#     def validate_action(self, request, queryset):
#         try:
#             for i in queryset.all():
#                 i.validate()
#         except PermissionError as err:
#             print(err)

#     validate_action.short_description = _('Validate selected Sales Orders')