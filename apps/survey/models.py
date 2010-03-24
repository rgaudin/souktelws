#!/usr/bin/env python
# encoding=utf-8

from django.db import models


class Person(models.Model):
    ''' Person Model represents result in the Survey '''

    MALE = 0
    FEMALE = 1
    SEXES = (
            (MALE, u"Male"),
            (FEMALE, u"Female"),
        )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=SEXES)
    age = models.PositiveIntegerField()
    activity = models.ForeignKey("Activity", blank=True, null=True)
    entered_on = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        ''' returns the full name '''
        return u"%(first)s %(last)s" % {'first': self.first_name.title(), \
                                        'last': self.last_name.upper()}

    @property
    def sex_name(self):
        ''' returns the human-readable version of sex '''
        for value, name in self.SEXES:
            if value == int(self.sex):
                return name
        return self.sex

    def __unicode__(self):
        return u"%(name)s %(age)s %(sex)s" \
               % {'name': self.name, 'age': self.age, 'sex': self.sex_name}


class Activity(models.Model):
    ''' Activity Model stores different activities with a unique code '''

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u"%s" % self.name
