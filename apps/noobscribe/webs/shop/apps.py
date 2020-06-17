from django.apps import AppConfig as AppConfigBase
from django.utils.translation import ugettext_lazy as _


class AppConfig(AppConfigBase):
    name = 'noobscribe.webs.shop'
    label = 'noobscribe_webs_shop'
    verbose_name = _('Noobscribe Webs Shop')