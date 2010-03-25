#!/usr/bin/env python
# encoding=utf-8

from django.contrib import admin

from models import Person, Activity

class PersonAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'sex_name', 'activity', 'entered_on')
    list_filter = ('activity', 'sex')
    ordering = [('-entered_on')]
    search_fields = ['first_name', 'last_name', 'activity__name']

class ActivityAdmin(admin.ModelAdmin):

    list_display = ('name', 'code')
    ordering = [('code')]

admin.site.register(Person, PersonAdmin)
admin.site.register(Activity, ActivityAdmin)
