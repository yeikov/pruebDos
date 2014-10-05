from django.conf.urls import patterns, url

urlpatterns = patterns('backend.views',
    url(r'^backend/$', 'evento_list'),
    url(r'^backend/(?P<pk>[0-9]+)/$', 'evento_detail'),
)
