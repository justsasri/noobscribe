from django.apps import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):
    name = 'noobwebs.accounts'
    label = 'noobwebs_accounts'
    verbose_name = 'NoobWebs Accounts'