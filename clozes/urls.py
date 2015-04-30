from django.conf.urls import url

from . import views

urlpatterns = [
    # Course index, ex: /
    url(r'^$', views.index, name='index'),
    # Deck index, ex: /5/
    url(r'^(?P<course_id>[0-9]+)/$', views.decks, name='decks'),
    # Main learning screen, ex: /5/14
    url(r'^(?P<course_id>[0-9]+)/(?P<deck_id>[0-9]+)/$', views.learn, name='learn'),
    # Update chunk (AJAX), ex: /5/14/502
    url(r'^(?P<course_id>[0-9]+)/(?P<deck_id>[0-9]+)/(?P<card_id>[0-9]+)/(?P<chunk_id>[0-9]+)/update$',
        views.update, name='update'),
]