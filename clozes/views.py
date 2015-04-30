from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Course, Deck, Card, TextChunk, BlankTextChunk


def index(request):
    course_list = Course.objects.all()
    return render(request, 'clozes/index.html', {'course_list': course_list})


def learn(request, course_id, deck_id):
    course = get_object_or_404(Course, pk=course_id)
    deck = get_object_or_404(Deck, pk=deck_id)
    card_list = deck.card_set.all()
    return render(request, 'clozes/learn.html', {'course': course, 'deck': deck, 'card_list': card_list})


def update(request, course_id, deck_id, card_id, chunk_id):
    blank = get_object_or_404(BlankTextChunk, pk=chunk_id)
    blank.update_user_feedback(request.post)
    return HttpResponse('')