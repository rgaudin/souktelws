#/usr/bin/env python
# encoding=utf-8

from django.contrib import admin
from models import Attendee, Group

class AttendeeAdmin(admin.ModelAdmin):

    list_display = ('first_name','last_name','email', 'group')
    list_filter = [('group'),]
    search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Group)
