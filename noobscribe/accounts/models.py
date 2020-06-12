import enum
import uuid
from django.db import models
from django.db.utils import cached_property
from django.db.models.signals import post_save
from django.utils import translation
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser

_ = translation.ugettext_lazy

class MemberLevel(enum.Enum):
    FREE = 0
    STARTER = 1
    POPULAR = 2
    ULTIMATE = 3

    CHOICES = (
        (FREE, _('free')),
        (STARTER, _('starter')),
        (POPULAR, _('popular')),
        (ULTIMATE, _('ultimate')),
    )

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
    membership = models.PositiveIntegerField(
        choices = MemberLevel.CHOICES.value,
        default = MemberLevel.FREE.value,
        verbose_name = _('membership'),
        help_text=_('Designates whether the user is a employee.'),
    )

    def natural_key(self):
        return (self.email,)