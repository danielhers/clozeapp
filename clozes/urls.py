from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<course_id>[0-9]+)/$', views.decks, name='decks'),
    # ex: /5/14
    url(r'^(?P<course_id>[0-9]+)/(?P<deck_id>[0-9]+)/$', views.learn, name='learn'),
]