from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobwebs.shop'
    label = 'noobwebs_shop'
    verbose_name = _('NoobWebs Shop')