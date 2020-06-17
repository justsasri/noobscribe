from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import MemberLevel

@admin.register(MemberLevel)
class MemberLevelAdmin(admin.ModelAdmin):
    list_display=['name']

# Register your models here.

admin.site.register(get_user_model(), UserAdmin)