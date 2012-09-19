from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    url(r'^world/', include('demo.world.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', direct_to_template, {'template':'overview.html'}),
    url(r'^about.html$', direct_to_template, {'template':'about.html'}),
    url(r'^get_it.html$', direct_to_template, {'template':'get_it.html'}),
    url(r'^overview.html$', direct_to_template, {'template':'overview.html'}),
    url(r'^details.html$', direct_to_template, {'template':'details.html'}),
    url(r'^device.html$', direct_to_template, {'template':'device.html'}),
)
