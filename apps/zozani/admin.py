#/usr/bin/env python
# encoding=utf-8

from django.contrib import admin
from models import Player

# personalisation de l'administration
class PlayerAdmin(admin.ModelAdmin):

    list_display = ('first_name','last_name')
    search_fields = ['first_name', 'last_name']

admin.site.register(Player, PlayerAdmin)
