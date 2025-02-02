from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    # English (default)
    question_en = models.TextField()
    answer_en = RichTextField()

    # Hindi
    question_hi = models.TextField(blank=True)
    answer_hi = RichTextField(blank=True)

    # Bengali
    question_bn = models.TextField(blank=True)
    answer_bn = RichTextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', self.question_en)

    def get_translated_answer(self, lang):
        return getattr(self, f'answer_{lang}', self.answer_en)

    def save(self, *args, **kwargs):
        translator = Translator()
        languages = ['hi', 'bn']
        for lang in languages:
            # Translate question
            if not getattr(self, f'question_{lang}'):
                translated = translator.translate(self.question_en, dest=lang).text
                setattr(self, f'question_{lang}', translated)
            # Translate answer (plain text for simplicity)
            if not getattr(self, f'answer_{lang}'):
                translated = translator.translate(self.answer_en, dest=lang).text
                setattr(self, f'answer_{lang}', translated)
        super().save(*args, **kwargs)