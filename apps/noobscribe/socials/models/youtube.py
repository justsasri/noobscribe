import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_qrcodes.models import QRCodeMixin

from .base import Category, SocialMedia


class YoutubeChannel(QRCodeMixin, SocialMedia):
    class Meta:
        verbose_name = _('youtube channel')
        verbose_name_plural = _('youtube channels')

    channel_id = models.CharField(
        max_length=32, unique=True,
        verbose_name=_('channel ID'),
        )
    view_counter = models.PositiveIntegerField(
        verbose_name=_('view counter'),
        help_text=_('total view gained')
        )
    primary = models.BooleanField(
        default=False,
        verbose_name=_("Primary"),
        help_text=_("People will subscribe and view this channel")
        )

    def __str__(self):
        return self.name

    def update(self, data):
        """ Update channel informations """
        pass

    def validate_show_subscriber(self):
        """ Make sure channel subscriber is public"""
        pass
    
    def validate_video_count(self):
        """ Make sure channel has at least 2 video"""
        pass

    def set_as_primary(self):
        """ Set this channel as primary """
        pass


class YoutubeVideo(QRCodeMixin, SocialMedia):
    class Meta:
        verbose_name = _('youtube video')
        verbose_name_plural = _('youtube videos')
    
    video_id = models.CharField(
        max_length=32, unique=True,
        verbose_name=_('video ID'),
        )
    primary = models.BooleanField(
        default=False,
        verbose_name=_("Primary"),
        help_text=_("Used as primary video campaign")
        )

    def __str__(self):
        return self.name

    def update(self, data):
        """ Update channel informations """
        pass

    def validate_show_subscriber(self):
        """ Make sure channel subscriber is public"""
        pass
    
    def validate_video_count(self):
        """ Make sure channel has at least 2 video"""
        pass

    def set_as_primary(self):
        """ Set this channel as primary """
        pass