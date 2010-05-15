#/usr/bin/env python
# encoding=utf-8

from django.contrib import admin
from models import Ligne,Arret,LigneArret

class LigneArretAdmin(admin.ModelAdmin):
    list_display = ('nomLigne','nomArret','ordre')

class LigneAdmin(admin.ModelAdmin):
    list_display = ('nomLigne',)

class ArretAdmin(admin.ModelAdmin):
    list_display = ('nomArret',)

admin.site.register(LigneArret, LigneArretAdmin)
admin.site.register(Ligne, LigneAdmin)
admin.site.register(Arret, ArretAdmin)
