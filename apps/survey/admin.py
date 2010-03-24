#!/usr/bin/env python
# encoding=utf-8

from django.contrib import admin

from models import Person, Activity

admin.site.register(Person)
admin.site.register(Activity)
