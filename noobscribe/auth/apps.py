from django.apps import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):
    name = 'noobscribe.auth'
    label = 'noobscribe_auth'
    verbose_name = 'Noobscribe Auth'