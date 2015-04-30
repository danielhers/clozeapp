from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, Deck, Card, TextChunk, BlankTextChunk


def index(request):
    course_list = Course.objects.all()
    output = ', '.join([c.name for c in course_list])
    return HttpResponse(output)


def decks(request, course_id):
    course = Course.objects.get(id=course_id)
    deck_list = course.deck_set.all()
    output = "Decks in course %s:\n" % course.name
    output += ', '.join([d.name for d in deck_list])
    return HttpResponse(output)


def learn(request, course_id, deck_id):
    course = Course.objects.get(id=course_id)
    deck = Deck.objects.get(id=deck_id)
    card_list = deck.card_set.all()
    output = "Cards in deck %s, in course %s:\n" % (deck.name, course.name)
    output += ', '.join([c.name for c in card_list])
    return HttpResponse(output)


def update(request, course_id, deck_id, card_id, chunk_id):
    course = Course.objects.get(id=course_id)
    deck = Deck.objects.get(id=deck_id)
    card = Card.objects.get(id=card_id)
    chunk = TextChunk.objects.get(id=chunk_id)
    return HttpResponse('')