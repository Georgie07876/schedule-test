from django.apps import AppConfig


class ScheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.schedule'

    def ready(self):
        from . import signals

        signals.connect_cache_invalidation_signals()
