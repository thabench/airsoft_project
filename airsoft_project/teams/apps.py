from django.apps import AppConfig


class TeamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teams'

    def ready(self):
        from .signals import create_profile, save_profile