from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the clozes index.")


def decks(request, course_id):
    response = "You're looking at the decks of course %s."
    return HttpResponse(response % course_id)


def learn(request, course_id, deck_id):
    response = "You're looking at a card in deck %s, under course %s."
    return HttpResponse(response % (deck_id, course_id))