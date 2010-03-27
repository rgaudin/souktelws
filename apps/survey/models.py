#!/usr/bin/env python
# encoding=utf-8

''' Survey App Models

Person: holds the encounters of Survey
Activity: Stores different activity runned by persons '''

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    ''' Person Model represents result in the Survey '''

    class Meta:
        verbose_name = _(u"Encounter")
        verbose_name_plural = _(u"Encounters")

    MALE = 0
    FEMALE = 1
    SEXES = (
            (MALE, _(u"Male")),
            (FEMALE, _(u"Female")),
        )

    first_name = models.CharField(verbose_name=_(u"First Name"), max_length=40)
    last_name = models.CharField(verbose_name=_(u"Last Name"), max_length=40)
    sex = models.CharField(verbose_name=_(u"Sex"), max_length=1, choices=SEXES)
    age = models.PositiveIntegerField(verbose_name=_(u"Age"))
    activity = models.ForeignKey("Activity", verbose_name=_(u"Occupation"), \
                                 blank=True, null=True, \
                                 help_text=u"Current Main Occupation")
    entered_on = models.DateTimeField(verbose_name="Date", \
                                      auto_now_add=True, \
                                      help_text=_("Date of encounter"))

    @property
    def name(self):
        ''' returns the full name '''
        return _(u"%(first)s %(last)s") % {'first': self.first_name.title(), \
                                        'last': self.last_name.upper()}

    @property
    def sex_name(self):
        ''' returns the human-readable version of sex '''
        for value, name in self.SEXES:
            if value == int(self.sex):
                return name
        return self.sex

    def __unicode__(self):
        return _(u"%(name)s %(age)s %(sex)s") \
               % {'name': self.name, 'age': self.age, 'sex': self.sex_name}


class Activity(models.Model):
    ''' Activity Model stores different activities with a unique code '''

    class Meta:
        verbose_name = _(u"Activity")
        verbose_name_plural = _(u"Activities")

    code = models.CharField(verbose_name=_(u"Code"), \
                            max_length=3, unique=True)
    name = models.CharField(verbose_name=_(u"Name"), \
                            max_length=30, help_text=_(u"Example: Student."))

    def __unicode__(self):
        return u"%s" % self.name
