from django.conf.urls import patterns, url

urlpatterns = patterns(
    'sigesti.views',
    url(r'^$', 'home', name='home'),
)
