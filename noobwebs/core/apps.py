from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobwebs.core'
    label = 'noobwebs_core'
    verbose_name = _('NoobWebs Core')