from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobscribe.core'
    label = 'noobscribe_core'
    verbose_name = _('NoobScribe Core')