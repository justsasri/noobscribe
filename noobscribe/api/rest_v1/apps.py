from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobscribe.api.rest_v1'
    verbose_name = _('NoobAPI v1')