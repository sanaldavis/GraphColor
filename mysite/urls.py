from django.conf.urls import patterns, include, url
from mysite.views import home

urlpatterns = patterns('',
    url('^$', home),
)
