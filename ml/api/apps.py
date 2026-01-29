from django.apps import AppConfig


class MlConfig(AppConfig):
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.ml.api'
    label = 'ml'
    verbose_name = 'ML'
    
    # def ready(self):
    #     """Инициализация модуля при загрузке"""
    #     pass
