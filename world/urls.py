from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'world.views.index', name='index'),
)
