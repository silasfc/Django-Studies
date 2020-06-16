from django.conf.urls import patterns, url
# from servers import views

urlpatterns = patterns(
    'servers.views',
    url(r'^$', 'server_list', name='server_list'),
    url(r'^new$', 'server_create', name='server_new'),
    url(r'^edit/(?P<pk>\d+)$', 'server_update', name='server_edit'),
    url(r'^delete/(?P<pk>\d+)$', 'server_delete', name='server_delete'),
)
