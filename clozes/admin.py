from django.contrib import admin

from .models import Course, Deck, Card, TextChunk

admin.site.register(Course)
admin.site.register(Deck)
admin.site.register(Card)
admin.site.register(TextChunk)