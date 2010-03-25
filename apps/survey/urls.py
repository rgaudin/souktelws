#!/usr/bin/env python
# encoding=utf-8

from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^survey/?$', views.index, name='index'),
    url(r'^survey/person/(?P<userid>\d+)/?$', views.person_detail, name='person-profile'),
)
