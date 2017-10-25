from django.apps import AppConfig
import os

default_app_config = 'cake.PrimaryCakeConfig'

VERBOSE_APP_NAME = u"蛋糕管理"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class PrimaryCakeConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME