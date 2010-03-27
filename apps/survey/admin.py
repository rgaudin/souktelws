#!/usr/bin/env python
# encoding=utf-8

''' Survey App Admin U.I '''

from django.contrib import admin

from models import Person, Activity

class PersonAdmin(admin.ModelAdmin):
    ''' Person Custom Admin U.I '''    

    list_display = ('name', 'age', 'sex_name', 'activity', 'entered_on')
    list_filter = ('activity', 'sex')
    ordering = [('-entered_on')]
    search_fields = ['first_name', 'last_name', 'activity__name']

class ActivityAdmin(admin.ModelAdmin):
    ''' Activity Custom Admin U.I '''

    list_display = ('name', 'code')
    ordering = [('code')]

admin.site.register(Person, PersonAdmin)
admin.site.register(Activity, ActivityAdmin)
