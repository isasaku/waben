from django.apps import AppConfig


class WabenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'waben'

    def ready(self):    #オーバーライド
        from .oder import start
        start()
