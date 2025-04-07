from django.apps import AppConfig


class DocumentappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.documentApp'
    def ready(self):
        import apps.documentApp.signals
