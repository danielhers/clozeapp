from django.db import models
from django.contrib.auth.models import User
from datetime import date

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

def save_sample_text(text, card):
    chunks = text.split("_")
    # TODO this is probably wrong
    i = 1;
    for chunk in chunks:
        is_blank = i % 2 == 0
        if is_blank:
            new_chunk = BlankTextChunk(id=1, next_appearance=date.today(), e_factor=1300)
        else:
            new_chunk = TextChunk(id=1)
        new_chunk.text = chunk
        new_chunk.card = card
        new_chunk.index = i

def insert_sample_data():
    # Create user
    sample_user = User.objects.create_user(username='daniel', email='dani@huji.com', password='1234')
    sample_course = Course(id=1, name="World History")
    sample_course.save()
    sample_deck = Deck(id=1, course=sample_course, user=sample_user, name='Contemporary History')
    sample_deck.save()
    sample_card = Card(id=1, deck=sample_deck, name='Wars', next_appearance=date.today())
    sample_card.save()
    sample_text1 = "The _first_ world war ended in 1917"
    save_sample_text(sample_text1, sample_card)
    sample_text2 = "The second world war started in _1939_ and ended in _1945"
    save_sample_text(sample_text2, sample_card)

if __name__ == "__main__":
    pass # populate DB with simple data