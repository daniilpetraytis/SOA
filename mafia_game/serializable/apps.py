from django.apps import AppConfig


class SerializableConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'serializable'
