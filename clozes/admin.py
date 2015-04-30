from django.contrib import admin

from .models import Course, Deck, Card, TextChunk, BlankTextChunk

admin.site.register(Course)
admin.site.register(Deck)
admin.site.register(Card)


class TextChunkAdmin(admin.ModelAdmin):
    fields = ['text', 'card', 'index']

admin.site.register(TextChunk, TextChunkAdmin)


class BlankTextChunkAdmin(admin.ModelAdmin):
    fields = ['text', 'card', 'index', 'next_appearance', 'e_factor']

admin.site.register(BlankTextChunk, BlankTextChunkAdmin)