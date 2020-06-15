import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_qrcodes.models import QRCodeMixin

from .base import Category, SocialMedia


class FacebookPage(QRCodeMixin, SocialMedia):
    class Meta:
        verbose_name = _('facebook page')
        verbose_name_plural = _('facebook pages')
        unique_together = ('owner', 'page_id')

    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        related_name='facebook_pages'
        )
    page_name = models.CharField(
        max_length=32, 
        null=True, blank=True,
        verbose_name=_('name')
        )
    page_id = models.CharField(
        max_length=32, unique=True,
        verbose_name=_('page ID')
        )
    primary = models.BooleanField(
        default=False,
        verbose_name=_("Primary"),
        help_text=_("People will like and view this channel")
        )

    def __str__(self):
        return self.channel_name

    def update(self, data):
        """ Update page informations """
        pass

    def validate_show_likes(self):
        """ Make sure page likes is public"""
        pass

    def set_as_primary(self):
        """ Set this page as primary """
        pass