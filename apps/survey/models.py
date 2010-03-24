#!/usr/bin/env python
# encoding=utf-8

from django.db import models


class Person(models.Model):
    ''' Person Model represents result in the Survey '''

    class Meta:
        verbose_name = u"Encounter"
        verbose_name_plural = u"Encounters"

    MALE = 0
    FEMALE = 1
    SEXES = (
            (MALE, u"Male"),
            (FEMALE, u"Female"),
        )

    first_name = models.CharField(verbose_name=u"First Name", max_length=40)
    last_name = models.CharField(verbose_name=u"Last Name", max_length=40)
    sex = models.CharField(verbose_name=u"Sex", max_length=1, choices=SEXES)
    age = models.PositiveIntegerField(verbose_name=u"Age")
    activity = models.ForeignKey("Activity", verbose_name=u"Occupation", blank=True, null=True, help_text=u"Current Main Occupation")
    entered_on = models.DateTimeField(verbose_name="Date", auto_now_add=True, help_text="Date of encounter")

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

    class Meta:
        verbose_name = u"Activity"
        verbose_name_plural = u"Activities"

    code = models.CharField(verbose_name=u"Code", max_length=3, unique=True)
    name = models.CharField(verbose_name=u"Name", max_length=30, help_text=u"Example: Student.")

    def __unicode__(self):
        return u"%s" % self.name
