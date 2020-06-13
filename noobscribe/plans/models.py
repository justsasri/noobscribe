import uuid
import enum
from django.db import models
from django.utils.translation import ugettext_lazy as _
from polymorphic.models import PolymorphicModel


class BalanceType(enum.Enum):
    FOLLOWER = 'FOLL'
    SUBSCRIBER = 'SUBS'
    VIEW = 'VIEW'

    CHOICES = (
        (FOLLOWER, _('follower')),
        (SUBSCRIBER, _('subscriber')),
        (VIEW, _('view')),
    )


class PlatformType(enum.Enum):
    YOUTUBE = 'YT'
    FACEBOOK = 'FB'
    INSTAGRAM = 'IG'

    CHOICES = (
        (YOUTUBE, _('youtube')),
        (FACEBOOK, _('facebook')),
        (INSTAGRAM, _('instagram')),
    )


class Plan(PolymorphicModel):
    class Meta:
        verbose_name = _('plan')
        verbose_name_plural = _('plans')

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid'
    )
    name = models.CharField(max_length=54, verbose_name=_('name'))
    validity = models.PositiveIntegerField(
        verbose_name=_('validity'),
        help_text=_('Validity in days')
    )
    history_limit = models.PositiveIntegerField(
        verbose_name=_('history limit'),
        help_text=_('History limit in days')
    )
    platform = models.CharField(
        max_length=4, editable=False,
        choices=PlatformType.CHOICES.value,
        default=PlatformType.YOUTUBE.value,
        verbose_name=_('platform')
    )
    balance_type = models.CharField(
        max_length=4, editable=False,
        choices=BalanceType.CHOICES.value,
        default=BalanceType.SUBSCRIBER.value,
        verbose_name=_('balance type')
    )
    gain_per_day = models.PositiveIntegerField(
        verbose_name=_('gain per day'),
        help_text=_('benefit gained per day')
    )
    give_per_day = models.PositiveIntegerField(
        verbose_name=_('give per day'),
        help_text=_('effort per day')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('price'),
        help_text=_('price per month')
    )
    email_report = models.BooleanField()
    whatsapp_report = models.BooleanField()

    def __str__(self):
        return self.name


class SubscriberYoutubePlan(Plan):
    class Meta:
        verbose_name = _('YouTube Subscriber')
        verbose_name_plural = _('YouTube Subscribers')

    def save(self, *args, **kwargs):
        self.platform = PlatformType.YOUTUBE.value
        self.balance_type = BalanceType.SUBSCRIBER.value
        super().save(*args, **kwargs)


class ViewYoutubePlan(Plan):
    class Meta:
        verbose_name = _('YouTube View')
        verbose_name_plural = _('YouTube Views')

    def save(self, *args, **kwargs):
        self.platform = PlatformType.YOUTUBE.value
        self.balance_type = BalanceType.VIEW.value
        super().save(*args, **kwargs)