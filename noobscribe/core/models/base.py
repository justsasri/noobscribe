from django.db import models
from django.utils import timezone, timesince
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class YoutubeChannel(models.Model):
    class Meta:
        verbose_name = _('youtube channel')
        verbose_name_plural = _('youtube channels')
        unique_together = ('owner', 'channel_id')
    
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid')
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        related_name='youtube_channels'
        )
    channel_id = models.CharField(
        max_length=32,
        verbose_name=_('channel ID')
        )
    balance_subcriber = models.IntegerField(
        default=0,
        verbose_name=_('balance subcriber')
        )
    balance_view = models.IntegerField(
        default=0,
        verbose_name=_('balance subcriber')
        )