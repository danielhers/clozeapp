from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import clozeapp.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', clozeapp.views.index, name='index'),
    url(r'^db', clozeapp.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
