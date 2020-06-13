from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobscribe.plans'
    label = 'noobscribe_plans'
    verbose_name = _('NoobScribe Plans')