#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin
from models import WeatherLocation
from models import WeatherSky
from models import Weather

admin.site.register(WeatherLocation)
admin.site.register(WeatherSky)
admin.site.register(Weather)

