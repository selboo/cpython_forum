from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cpython_forum.views.index', name='home'),
    # url(r'^cpython_forum/', include('cpython_forum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/',include('grappelli.urls')),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT , 'show_indexes':True}),

)

urlpatterns += patterns('',
	 (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
	 (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
	 (r'^accounts/register/$', 'cpython_forum.views.register'),

)
