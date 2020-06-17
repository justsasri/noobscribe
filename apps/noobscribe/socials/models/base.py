import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_qrcodes.models import QRCodeMixin
from django.core.exceptions import ValidationError

from polymorphic.models import PolymorphicModel
from mptt.models import MPTTModel, TreeForeignKey
from taggit.models import TaggedItemBase, TagBase
from taggit.managers import TaggableManager

from noobscribe.core.utils.slugify import unique_slugify

class Category(MPTTModel):
    class Meta:
        ordering = ['name']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    name = models.CharField(
        max_length=80, unique=True, verbose_name=_('Category Name'))
    slug = models.SlugField(unique=True, max_length=80)
    parent = TreeForeignKey(
        'self', blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name="children",
        help_text=_(
            'Categories, unlike tags, can have a hierarchy. You might have a '
            'Jazz category, and under that have children categories for Bebop'
            ' and Big Band. Totally optional.'), )
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    @property
    def opts(self):
        return self._meta

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError('Parent category cannot be self.')
            if parent.parent and parent.parent == self:
                raise ValidationError('Cannot have circular Parents.')

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class Tag(TagBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    @property
    def opts(self):
        return self._meta


class SocialMedia(PolymorphicModel):
    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Medias")

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
    name = models.CharField(
        max_length=32,
        null=True, blank=True,
        verbose_name=_('name')
        )
    url = models.URLField(
        null=True, blank=True,
        verbose_name=_('url')
        )
    thumbnail = models.URLField(
        null=True, blank=True,
        verbose_name=_('thumbnail')
        )
    category = models.ForeignKey(
        Category, related_name='social_medias',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name=_("Category"))
    tags = TaggableManager(
        through='TaggedMedia',
        blank=True,
        related_name='social_medias',
        verbose_name=_("Tags"))
    subscriber_counter = models.PositiveIntegerField(
        verbose_name=_('subscriber counter'),
        help_text=_('total subscriber gained')
        )
        
    def validate_ownership(self):
        """ Validate channel owner """
        pass


class TaggedMedia(TaggedItemBase):
    class Meta:
        verbose_name = _("Tagged Media")
        verbose_name_plural = _("Tagged Medias")

    content_object = models.ForeignKey(
        SocialMedia, on_delete=models.CASCADE,
        related_name='tagged_medias')
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE,
        related_name="tagged_products")