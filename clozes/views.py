from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Course, Deck, BlankTextChunk


def index(request):
    course_list = Course.objects.all()
    return render(request, 'clozes/index.html', {'course_list': course_list})


def learn(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    card = deck.next_card()
    return render(request, 'clozes/learn.html', {'card': card})


def update(request, chunk_id):
    blank = get_object_or_404(BlankTextChunk, pk=chunk_id)
    blank.update_user_feedback(request.post)
    return HttpResponse('')