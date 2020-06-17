import enum
import uuid
from django.db import models
from django.db.utils import cached_property
from django.db.models.signals import post_save
from django.utils import translation
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django_numerators.models import NumeratorMixin

_ = translation.ugettext_lazy


class User(AbstractUser):
    
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid')
    email = models.EmailField(_('email address'), blank=False, unique=True)
    title = models.CharField(_('title'), max_length=30, blank=False)
    first_name = models.CharField(_('full name'), max_length=30, blank=False)

    is_superuser = models.BooleanField(
        _('superuser'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    def natural_key(self):
        return (self.email,)


class MemberLevel(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid')
    name = models.CharField(
        max_length=30,
        blank=False,
        verbose_name=_('full name'),)
    history_limit = models.PositiveIntegerField(
        verbose_name=_('history limit'),
        help_text=_('History limit in days')
        )
    subcriber_gain = models.PositiveIntegerField(
        verbose_name=_('subcriber gained'),
        help_text=_('subcriber gained per day')
        )
    subcriber_give = models.PositiveIntegerField(
        verbose_name=_('subcribe give'),
        help_text=_('Subscribe other channel')
        )
    view_gain = models.PositiveIntegerField(
        verbose_name=_('viewer gained'),
        help_text=_('subcriber gained per day')
        )
    view_give = models.PositiveIntegerField(
        verbose_name=_('view give'),
        help_text=_('Wathc people video')
        )
    fan_gain = models.PositiveIntegerField(
        verbose_name=_('fan gain'),
        help_text=_('Fan gained per day')
        )
    fan_give = models.PositiveIntegerField(
        verbose_name=_('fan give'),
        help_text=_('Become other fan')
        )
    email_report = models.BooleanField()

    def __str__(self):
        return self.name


class Member(NumeratorMixin, models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name='uuid')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name = _('user')
        )
    membership = models.ForeignKey(
        MemberLevel, 
        null=True, blank=False,
        on_delete=models.PROTECT,
        verbose_name = _('membership'),
        help_text=_('Designates whether the user is a employee.'),
        )
    validity = models.PositiveIntegerField(
        verbose_name=_('validity'),
        help_text=_('Validity in days')
        )