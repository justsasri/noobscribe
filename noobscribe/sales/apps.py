from django.apps import AppConfig as AppConfigBase


class AppConfig(AppConfigBase):
    name = 'noobscribe.sales'
    label = 'noobscribe_sales'
    verbose_name = 'Noobscribe Sales'
