from django.conf.urls import patterns, include, url
from client.views import *

urlpatterns = patterns('',
  url(r'^$', index, name='index'),
  url(r'^studios$', studios, name='studios'),
  url(r'^studio/(\w+)/$', studio, name='studio'),
)
