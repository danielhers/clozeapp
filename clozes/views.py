from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, Deck, Card, TextChunk, BlankTextChunk


def index(request):
    course_list = Course.objects.all()
    return render(request, 'clozes/index.html', {'course_list': course_list})


def decks(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    deck_list = course.deck_set.all()
    return render(request, 'clozes/decks.html', {'course': course, 'deck_list': deck_list})


def learn(request, course_id, deck_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    try:
        deck = course.deck_set.get(id=deck_id)
    except Deck.DoesNotExist:
        raise Http404("Deck does not exist")

    card_list = deck.card_set.all()
    return render(request, 'clozes/learn.html', {'course': course, 'deck': deck, 'card_list': card_list})


def update(request, course_id, deck_id, card_id, chunk_id):
    course = Course.objects.get(id=course_id)
    deck = Deck.objects.get(id=deck_id)
    card = Card.objects.get(id=card_id)
    chunk = TextChunk.objects.get(id=chunk_id)
    return HttpResponse('')