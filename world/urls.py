from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'demo.world.views.index', name='index'),
)
