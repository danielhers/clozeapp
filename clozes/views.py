from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Course, Deck, Card, BlankTextChunk


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
    return HttpResponse()


def insert(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    if request.method == 'POST':
        deck.add_card(request.POST['name'], request.POST['text'])
        return HttpResponseRedirect(reverse('learn', args=(deck_id,)))
    return render(request, 'clozes/insert.html', {'deck': deck})


def skip(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.method == 'POST':
        card.skip()
        return HttpResponseRedirect(reverse('learn', args=(card.deck.id,)))
    return HttpResponse()


def list(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    return render(request, 'clozes/list.html', {'deck': deck})