from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import login,logout,password_change,password_change_done
import django.contrib.auth.views
from client.views import *
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^', include('client.urls')),
  url(r'^content/', include('content.urls')),
  #url(r'^accounts/', include('members.urls')),
  (r'^accounts/', include('registration.backends.default.urls')),
  url(r'^admin/', include(admin.site.urls)),

)
