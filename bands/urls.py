# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^bands/$', band_listing, name='bands'),
    url(r'^bands/(?P<pk>\d+)/$', band_detail, name='band_detail'),
    url(r'^bandform/$', BandForm.as_view(), name='band_form'),
    url(r'^memberform/$', MemberForm.as_view(), name='member_form'),
    url(r'^contact/$', band_contact, name='contact'),
    url(r'^protected/$', protected_view, name='protected'),
    url(r'^accounts/login/$', message, name='message')
]
