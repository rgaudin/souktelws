#/usr/bin/env python
# encoding=utf-8

from django.db import models

class Attendee(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    group = models.ForeignKey("Group", blank=True, null=True)

    number = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return u"%(first)s %(last)s" % {'first': self.first_name.title(), \
                                       'last': self.last_name.title()}

class Group(models.Model):

    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
