from django.apps import AppConfig


class FaqConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faq'
# myproject/apps.py
from django.apps import AppConfig

class MyAdminConfig(AppConfig):
    name = 'myproject'  
    label = 'myproject_custom' 
class FaqConfig(AppConfig):
    name = 'faq'
    def ready(self):
        import faq.signals