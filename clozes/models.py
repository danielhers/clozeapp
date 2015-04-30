from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)

class Course(models.Model):
    name = models.CharField(max_length=50)

class Deck(models.Model):
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)

class Card(models.Model):
    deck = models.ForeignKey(Deck)
    name = models.CharField(max_length=50)
    next_appearance = models.DateField()
    e_factor = models.IntegerField()

class TextChunk(models.Model):
    card = models.ForeignKey(Card)
    index = models.IntegerField()
    next_appearance = models.DateField()
    e_factor = models.IntegerField()

