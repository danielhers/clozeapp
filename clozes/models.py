from django.db import models
from django.contrib.auth.models import User

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

class TextChunk(models.Model):
    text = models.TextField()
    card = models.ForeignKey(Card)
    index = models.IntegerField()

class BlankTextChunk(TextChunk):
    next_appearance = models.DateField()
    e_factor = models.IntegerField()

if __name__ == "__main__":
    pass # populate DB with simple data