from django.conf.urls import url

from . import views

urlpatterns = [
    # Course index, ex: /
    url(r'^$', views.index, name='index'),
    # Deck index, ex: /5/
    url(r'^(?P<deck_id>[0-9]+)/$', views.learn, name='learn'),
    # Update chunk (AJAX), ex: /5/14/502
    url(r'^update/(?P<chunk_id>[0-9]+)/$',
        views.update, name='update'),
]