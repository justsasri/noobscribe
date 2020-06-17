from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobscribe.socials'
    label = 'noobscribe_socials'
    verbose_name = _('Noobscribe Socials')