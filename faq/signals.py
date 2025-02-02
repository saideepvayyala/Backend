from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import FAQ

@receiver([post_save, post_delete], sender=FAQ)
def clear_faq_cache(sender, **kwargs):
    for lang in ['en', 'hi', 'bn']:
        cache.delete(f'faqs_{lang}')