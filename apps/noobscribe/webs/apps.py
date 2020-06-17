from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobscribe.webs'
    label = 'noobscribe_webs'
    verbose_name = _('Noobscribe Webs')