from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin
    )
from .models import (
    Plan, 
    SubscriberYoutubePlan,
    ViewYoutubePlan
    )


@admin.register(SubscriberYoutubePlan)
class SubscriberYoutubePlanAdmin(PolymorphicChildModelAdmin):
    base_model = Plan


@admin.register(ViewYoutubePlan)
class ViewYoutubePlanAdmin(PolymorphicChildModelAdmin):
    base_model = Plan


@admin.register(Plan)
class PlanAdmin(PolymorphicParentModelAdmin):
    child_models = [
        SubscriberYoutubePlan,
        ViewYoutubePlan
    ]
    list_display = [
        'name',
        'validity',
        'history_limit',
        'platform',
        'balance_type',
        'gain_per_day',
        'give_per_day',
        'price',
        'email_report',
        'whatsapp_report',
    ]