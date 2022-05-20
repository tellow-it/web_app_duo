from modeltranslation.translator import register, TranslationOptions
from .models import Post


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ('title', 'author', 'content', 'created_on', 'updated_on')
