from django.contrib import admin
from .models import *


class BitsModel(admin.ModelAdmin):
    list_display = ('username', 'code')
    list_filter = ('username', 'code')
    search_fields = ['name', 'code']


class ContentModel(admin.ModelAdmin):
    list_display = ('timestamp', 'bits',)
    list_filter = ('bits',)
    search_fields = ['content']


admin.site.register(Bits, BitsModel)
admin.site.register(Content, ContentModel)
