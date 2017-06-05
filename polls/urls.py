# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'polls.views',
    url(r'^$', 'index', name='index'),
)
