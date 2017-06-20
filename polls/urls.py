# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
# ou ... from views import index

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ou ... url(r'^$', index, name='index'),
]
