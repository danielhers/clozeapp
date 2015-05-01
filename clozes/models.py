# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.db.models import Min

INITIAL_E_FACTOR = 2500
MIN_E_FACTOR = 1300
E_FACTOR_CHANGE = 200
INTERVALS = [1, 2]


class Course(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField("Image", upload_to="img/", default="img/button_c.png")


class Deck(models.Model):
    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    def next_card(self):
        card_set = self.card_set
        min_next = card_set.aggregate(Min('next_appearance'))['next_appearance__min']
        if min_next > date.today():
            return None
        card_list = card_set.filter(next_appearance__gte=min_next)
        card_list = [card for card in card_list if any(chunk.is_hidden for chunk in card.chunks)]
        if not card_list:
            return None
        return card_list[0]
    
    def add_card(self, card_name, text):
        new_card = Card(id=None, deck=self, name=card_name, next_appearance=date.today())
        new_card.save()
        chunks = text.split("_")
        for i, chunk in enumerate(chunks):
            is_blank = i % 2 == 1
            if is_blank:
                new_chunk = BlankTextChunk(id=None,
                                           next_appearance=date.today(),
                                           e_factor=INITIAL_E_FACTOR)
            else:
                new_chunk = TextChunk(id=None)
            new_chunk.text = chunk
            new_chunk.card = new_card
            new_chunk.index = i
            new_chunk.save()

        new_card.update_next_appearance()

    @property
    def normal_score(self):
        # Get average score of blanks
        blank_scores = []
        for card in self.card_set.all():
            for blank in card.textchunk_set.filter(blanktextchunk__next_appearance__isnull=False):
                blank_scores.append(blank.blanktextchunk.e_factor)
        average = sum(blank_scores, 0.0) / len(blank_scores)
        max_x = max(blank_scores)
        min_x = min(blank_scores)
        MINIMUM_SCORE = 1300
        MAXIMUM_SCORE = 2500
        scaled = [((MAXIMUM_SCORE - MINIMUM_SCORE)*(x - min_x))/(max_x - min_x) + MINIMUM_SCORE for x in blank_scores]
        return average(scaled)


class Card(models.Model):
    deck = models.ForeignKey(Deck)
    name = models.CharField(max_length=50)
    next_appearance = models.DateField()

    def update_next_appearance(self):
        blanks = self.textchunk_set.filter(blanktextchunk__next_appearance__isnull=False)
        self.next_appearance = blanks.aggregate(Min('blanktextchunk__next_appearance')).values()[0]
        if self.next_appearance is None:
            raise ValueError("Card has no blanks")
        self.save()

    def skip(self):
        self.next_appearance = date.today() + timedelta(days=1)

    @property
    def days_left(self):
        d = self.next_appearance - date.today()
        return d.days

    @property
    def chunks(self):
        return self.textchunk_set.order_by('index').all()


class TextChunk(models.Model):
    text = models.TextField()
    card = models.ForeignKey(Card)
    index = models.IntegerField()

    @property
    def is_hidden(self):
        try:
            b = BlankTextChunk.objects.get(pk=self.id)
            return b.next_appearance <= date.today()
        except BlankTextChunk.DoesNotExist:
            return False

    def __str__(self):
        return self.text


class BlankTextChunk(TextChunk):
    next_appearance = models.DateField()
    e_factor = models.IntegerField()
    last_interval = models.IntegerField(default=INTERVALS[0])

    def update_user_feedback(self, user_rating):
        (interval, new_e_factor) = interval_algorithm(self.e_factor, self.last_interval, user_rating)
        self.last_interval = interval
        self.next_appearance += timedelta(interval)
        self.e_factor = new_e_factor
        self.save()
        self.card.update_next_appearance()


def interval_algorithm(e_factor, last_interval, user_rating):
    if user_rating == 0:
        return INTERVALS[0], e_factor
    elif user_rating == 2:
        e_factor = max(MIN_E_FACTOR, e_factor + E_FACTOR_CHANGE)
    return int(round(last_interval * e_factor / 1000)), e_factor


def insert_sample_data():
    # Create user
    sample_user = User.objects.create_user(username='daniel', email='dani@huji.com', password='1234')

    course_names = [u"שפת C", u"היסטוריה עולמית", u"כימיה אורגנית"]
    sample_courses = []

    for i, course_name in enumerate(course_names):
        sample_course = Course(id=None, name=course_name)
        sample_course.save()
        sample_courses.append(sample_course)

    deck_names = [u"היסטוריה עכשווית", u"המהפכה הצרפתית", u"ימי הביניים", u"העת העתיקה"]
    for i, deck_name in enumerate(deck_names):
        Deck(id=None, course=sample_courses[0], user=sample_user, name=deck_name).save()

    deck_names = [u"פוינטרים", u"טיפוסי משתנים", u"פונקציות"]
    for i, deck_name in enumerate(deck_names):
        Deck(id=None, course=sample_courses[2], user=sample_user, name=deck_name).save()

    sample_deck = Deck.objects.get(name=u"היסטוריה עכשווית")
    sample_text1 = u"מלחמת העולם _הראשונה_ הסתיימה בשנת 1917"
    sample_deck.add_card(u"מלחמה", sample_text1)
    sample_text2 = u"מלחמת העולם השנייה פרצה בשנת _1939_ ותמה בשנת _1945_"
    sample_deck.add_card(u"מלחמה", sample_text2)

    sample_deck = Deck.objects.get(name=u"פוינטרים")
    for i in range(1, 5):
        sample_file = "data/c_sample%d.txt" % i
        with open(sample_file) as f:
            name = f.readline()
            f.readline()
            text = f.readline()
        sample_deck.add_card(name, text)

if __name__ == "__main__":
    pass   # populate DB with simple data