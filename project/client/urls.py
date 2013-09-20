from django.conf.urls import patterns, include, url
from client.views import *

urlpatterns = patterns('',
  url(r'^$', index, name='index'),
  url(r'^class/$', forbidden, name='class'),
  url(r'^pay/$', pay, name='pay'),
)
