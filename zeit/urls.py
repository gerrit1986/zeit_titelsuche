# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.conf import settings
# from django.views.static import *
from search.views import ClassView

admin.autodiscover()

urlpatterns = patterns('',
                    url(r'^$', 'search.views.home', name='home'),
                    url(r'^home/', 'search.views.home', name='home'),
                    url(r'^query/$', 'search.views.home', name='home'),
                    url(r'^query/([^/]+)/$', 'search.views.query', name='query'),
                    url(r'^admin/', include(admin.site.urls)),
                    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                    (r'^class-based/([^/]+)/$', ClassView.as_view()),
                    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)