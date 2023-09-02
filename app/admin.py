from django.contrib.admin import *
from .models import (
    Client,
    Blog,
    Sponsor,
    Product
)
from modeltranslation.admin import TranslationAdmin

@register(Client)
class ClientAdmin(ModelAdmin):

    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')
    ordering = ('fullname',)

@register(Blog)
class BlogAdmin(TranslationAdmin):

    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title', 'date')
    ordering = ('-date',)

@register(Sponsor)
class SponsorAdmin(ModelAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name',)

@register(Product)
class ProductAdmin(TranslationAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name',)