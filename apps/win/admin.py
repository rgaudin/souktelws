#!/usr/bin/env python
# encoding=utf-8

from django.contrib import admin

from models import Game, Question, Player, Participation

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Player)
admin.site.register(Participation)
