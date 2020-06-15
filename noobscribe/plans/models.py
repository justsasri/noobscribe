import uuid
import enum
from django.db import models
from django.utils.translation import ugettext_lazy as _
from polymorphic.models import PolymorphicModel, PolymorphicManager
from noobscribe.auth.models import MemberLevel


class BalanceType(enum.Enum):
    FAN = 'FANS'
    FOLLOWER = 'FOLL'
    SUBSCRIBER = 'SUBS'
    COMMENT = 'COMM'
    LIKE = 'LIKE'
    DISLIKE = 'DISL'
    VIEW = 'VIEW'

    CHOICES = (
        (FAN, _('Fan')),
        (FOLLOWER, _('Follower')),
        (SUBSCRIBER, _('Subscriber')),
        (COMMENT, _('Comment')),
        (LIKE, _('Like')),
        (DISLIKE, _('Dislike')),
        (VIEW, _('View')),
    )


class PlatformType(enum.Enum):
    YOUTUBE = 'YT'
    FACEBOOK = 'FB'
    INSTAGRAM = 'IG'
    SOUNDCLOUD = 'SC'

    CHOICES = (
        (YOUTUBE, _('Youtube')),
        (FACEBOOK, _('Facebook')),
        (INSTAGRAM, _('Instagram')),
        (SOUNDCLOUD, _('SoundCloud')),
    )


class ProductManager(PolymorphicManager):

    def get_queryset(self):
        return super().get_queryset().non_polymorphic()


class Product(PolymorphicModel):
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('product')

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid'
    )
    name = models.CharField(max_length=54, verbose_name=_('name'))
    unit_of_measure = models.CharField(
        max_length=25, null=True, blank=False,
        verbose_name=_('unit')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('price'),
        help_text=_('price per month')
    )

    def __str__(self):
        return self.name


class Membership(Product):
    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Member')

    member_level = models.ForeignKey(
        MemberLevel, on_delete=models.CASCADE,
        null=True, blank=False, # Todo Must not null 
        related_name='products',
        verbose_name=_('member level')
        )
    validity = models.PositiveIntegerField(
        verbose_name=_('validity'),
        help_text=_('validity')
        )

    def __str__(self):
        return self.name


class Quota(Product):
    class Meta:
        verbose_name = _('Quota')
        verbose_name_plural = _('Quota')

    platform = models.CharField(
        max_length=4,
        choices=PlatformType.CHOICES.value,
        default=PlatformType.YOUTUBE.value,
        verbose_name=_('platform')
    )
    balance_type = models.CharField(
        max_length=4,
        choices=BalanceType.CHOICES.value,
        default=BalanceType.SUBSCRIBER.value,
        verbose_name=_('balance type')
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_('quantity'),
        help_text=_('quantity')
        )

    def __str__(self):
        return self.name