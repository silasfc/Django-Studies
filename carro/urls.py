# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'carro.views',
    url(r'^$', 'index', name='index'),
    # url(r'^(\d+)/$', 'details', name='details'),
    # url(r'^(\d+)/delete$', 'delete', name='delete')
)
