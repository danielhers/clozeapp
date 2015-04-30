from django.conf.urls import url

from . import views

urlpatterns = [
    # Course index, ex: /
    url(r'^$', views.index, name='index'),
    # Deck index, ex: /learn/5/
    url(r'^learn/(?P<deck_id>[0-9]+)/$', views.learn, name='learn'),
    # Deck index, ex: /insert/5/
    url(r'^insert/(?P<deck_id>[0-9]+)/$', views.insert, name='insert'),
    # Update chunk (AJAX), ex: /update/504
    url(r'^update/(?P<chunk_id>[0-9]+)/$',
        views.update, name='update'),
]