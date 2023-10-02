from django.apps import AppConfig

class EmailsenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emailSender'

    def ready(self):
        from . import signals
