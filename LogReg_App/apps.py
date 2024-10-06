from django.apps import AppConfig


class LogregAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LogReg_App'

# from django.apps import AppConfig

# class AccountsConfig(AppConfig):
#     name = 'LogReg_App'

#     def ready(self):
#         import LogReg_App.signals
