from django.apps import AppConfig


class OlchaShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'olcha_shop'

    def ready(self):
        import olcha_shop.signals
