from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import (password_reset, password_reset_done, password_change, password_change_done)
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    url(r'^world/', include('world.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook/', include('django_facebook.urls')),
    #url(r'^accounts/', include('registration.urls')),

    url(r'^$', direct_to_template, {'template':'overview.html'}),
    url(r'^about.html$', direct_to_template, {'template':'about.html'}),
    url(r'^get_it.html$', direct_to_template, {'template':'get_it.html'}),
    url(r'^overview.html$', direct_to_template, {'template':'overview.html'}),
    url(r'^details.html$', direct_to_template, {'template':'details.html'}),
    url(r'^device.html$', direct_to_template, {'template':'device.html'}),
)

urlpatterns += patterns('',
  (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
  (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
  (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
  (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
  (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

