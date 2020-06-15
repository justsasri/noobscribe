from django.contrib import admin

from .models import YoutubeChannel

@admin.register(YoutubeChannel)
class YoutubeChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_name', 'owner', 'channel_id']