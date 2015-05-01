from django.conf.urls import url

from . import views

urlpatterns = [
    # Course index, ex: /
    url(r'^$', views.index, name='index'),
    # Deck index, ex: /learn/5/
    url(r'^learn/(?P<deck_id>[0-9]+)/$', views.learn, name='learn'),
    # Update chunk (AJAX), ex: /update/504
    url(r'^update/(?P<chunk_id>[0-9]+)/$', views.update, name='update'),
    # Insert new card to deck, ex: /insert/5/
    url(r'^insert/(?P<deck_id>[0-9]+)/$', views.insert, name='insert'),
    # Skip card to get the next one, ex: /insert/24/
    url(r'^skip/(?P<card_id>[0-9]+)/$', views.skip, name='skip'),
    # List cards in deck, ex: /list/5/
    url(r'^list/(?P<deck_id>[0-9]+)/$', views.list, name='list'),
]