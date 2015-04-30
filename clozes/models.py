# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from django.db.models import Min


class Course(models.Model):
    name = models.CharField(max_length=50)


class Deck(models.Model):
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    def next_card(self):
        card_set = self.card_set
        min_next = card_set.aggregate(Min('next_appearance'))['next_appearance__min']
        return card_set.get(next_appearance=min_next)


class Card(models.Model):
    deck = models.ForeignKey(Deck)
    name = models.CharField(max_length=50)
    next_appearance = models.DateField()

    def update_next_appearance(self):
        blanks = Card.objects.all()[0].textchunk_set.filter(blanktextchunk__next_appearance__isnull=False)
        self.next_appearance = blanks.aggregate(Min('blanktextchunk__next_appearance')).values()[0]
        self.save()


class TextChunk(models.Model):
    text = models.TextField()
    card = models.ForeignKey(Card)
    index = models.IntegerField()

    @property
    def is_hidden(self):
        try:
            b = BlankTextChunk.objects.get(pk=self.id)
            return b.next_appearance > datetime.date(datetime.now())
        except BlankTextChunk.DoesNotExist:
            return False

    def __str__(self):
        return self.text


class BlankTextChunk(TextChunk):
    next_appearance = models.DateField()
    e_factor = models.IntegerField()

    def update_user_feedback(self, feedback):
        (interval, new_e_factor) = dummy_interval_algorithm(self, feedback)
        self.next_appearance += interval
        self.e_factor = new_e_factor
        self.card.update_next_appearance()


def dummy_interval_algorithm(blank, feedback):
    return 2


def save_sample_text(text, card):
    chunks = text.split("_")
    # TODO this is probably wrong
    for i, chunk in enumerate(chunks):
        is_blank = i % 2 == 1
        if is_blank:
            new_chunk = BlankTextChunk(id=i, next_appearance=date.today() + timedelta(days=i), e_factor=1300)
        else:
            new_chunk = TextChunk(id=i)
        new_chunk.text = chunk
        new_chunk.card = card
        new_chunk.index = i
        new_chunk.save()
    card.update_next_appearance()


def insert_sample_data():
    # Create user
    sample_user = User.objects.create_user(username='daniel', email='dani@huji.com', password='1234')
    sample_course = Course(id=1, name="היסטוריה עולמית")
    sample_course.save()
    sample_deck = Deck(id=1, course=sample_course, user=sample_user, name='היסטוריה עכשווית')
    sample_deck.save()
    sample_card = Card(id=1, deck=sample_deck, name='מלחמות העולם', next_appearance=date.today())
    sample_card.save()
    sample_text1 = "מלחמת העולם _הראשונה_ הסתיימה בשנת 1917"
    save_sample_text(sample_text1, sample_card)
    sample_text2 = "מלחמת העולם השנייה פרצה בשנת _1939_ ותמה בשנת _1945_"
    save_sample_text(sample_text2, sample_card)