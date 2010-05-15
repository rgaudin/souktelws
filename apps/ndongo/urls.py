#!/usr/bin/env python
# encoding=utf-8

from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^ndongo/?$', views.index, name='index'),
)
