from modeltranslation.translator import TranslationOptions, register

from apps.common.models import Contact, Ad, StaticPage
from django.conf import settings as base


@register(StaticPage)
class StaticPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = base.MODELTRANSLATION_LANGUAGES


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = base.MODELTRANSLATION_LANGUAGES


@register(Ad)
class AdTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = base.MODELTRANSLATION_LANGUAGES
