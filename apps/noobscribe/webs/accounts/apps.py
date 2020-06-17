from django.apps import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):
    name = 'noobscribe.webs.accounts'
    label = 'noobscribe_webs_accounts'
    verbose_name = 'Noobscribe Webs Accounts'