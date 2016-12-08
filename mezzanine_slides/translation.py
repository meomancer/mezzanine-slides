__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/12/16'
from modeltranslation.translator import translator, TranslationOptions
from .models import Slide


class SlideEvent(TranslationOptions):
    fields = ('caption', 'description',)


translator.register(Slide, SlideEvent)
