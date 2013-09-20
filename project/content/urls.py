from django.conf.urls import patterns, include, url
from content.views import *

urlpatterns = patterns('',
  url(r'^chapter/(\d)/$', chapter, name='chapter'),
  url(r'^page/(\d)/$', page, name='page'),
)
