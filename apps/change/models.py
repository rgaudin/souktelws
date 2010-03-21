#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin


from django.db import models

class Currency(models.Model):

    code = models.CharField(max_length=5)
    rate = models.DecimalField(max_digits=5, decimal_places=2)



    def __unicode__(self):
        return u"%s (%s)" % (self.code, self.rate)
