from .models import (
    Blog,
    Product, 
)
from modeltranslation.translator import TranslationOptions, register

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')