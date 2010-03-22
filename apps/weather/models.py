#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin


from django.db import models


	

class WeatherLocation(models.Model) : 

    code = models.CharField(max_length=5, unique=True)
    name=   models.CharField(max_length=20)
    
    def __unicode__(self):
	    return u"%s (%s)" % (self.code, self.name)


class WeatherSky(models.Model) :

    code = models.CharField(max_length=5, unique=True)
    name=   models.CharField(max_length=20)

    def __unicode__(self):
	    return u"%s (%s)" % (self.code, self.name)


class Weather(models.Model):

    class Meta:
	    unique_together = ('weatherLocation', 'dayofweek')

    weatherLocation = models.ForeignKey(WeatherLocation)
    dayofweek = models.CharField(max_length=3)
    sky = models.ForeignKey(WeatherSky)
    temp= models.DecimalField(max_digits=2, decimal_places=0)



    def __unicode__(self):
        return u"%s (%s)"% (self.sky,self.temp)

