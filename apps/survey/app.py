#!/usr/bin/env python
# encoding=utf-8

''' Survey RapidSMS App '''

import rapidsms
from rapidsms.parsers.keyworder import Keyworder
from django.utils.translation import ugettext as _

from models import *


class App(rapidsms.app.App):
    ''' Survey RapidSMS App

    Manages one simple SMS-collected survey.

    help: return usage
    survey: record an encounter
    find: look up results from DB.
    stat: return number of records '''

    keyword = Keyworder()

    def handle(self, message):
        ''' finds out corresponding function and call it

        Use the Keyworder parser '''

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            self.log('INFO', u"Survey: not catched")
            return False

        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(_(u"Survey System Error: %s") % e)
            return True

    keyword.prefix = ['help', _(u"help")]

    @keyword('')
    def help(self, message):
        ''' display a usage message for the survey '''

        message.respond(_(u"Survey format: survey FIRST LAST SEX AGE (ACTIVITY)"))
        return True

    keyword.prefix = ['survey', 'fill', _(u"survey")]

    @keyword(r'(\w+) (\w+) (\w) (\d+)\s?(\w*)')
    def fill(self, message, first, last, sex, age, activity_code):
        ''' Enters a survey item into the DB '''

        message.respond(sex)
        # parse appropriate sex type
        if sex.lower() in ('m', _(u"m")):
            sex = Person.MALE
        else:
            sex = Person.FEMALE

        # convert age to int
        age = int(age)

        # retrieve activity (or None)
        try:
            activity = Activity.objects.get(code=activity_code.strip().lower())
        except Activity.DoesNotExist:
            activity = None

        # create person object then save it.
        person = Person(first_name=first, last_name=last, sex=sex, \
                        age=age, activity=activity)
        person.save()

        message.respond(_(u"Thank you %(name)s for taking the survey. " \
                        "Your ID is %(id)s") \
                        % {'name': person.name, 'id': person.id})
        return True

    keyword.prefix = ['find', _(u"find")]
    @keyword('(\w+)')
    def search(self, message, activity_code):
        ''' find the result of people in DB filtered by activity '''

        # if activity is not found, use None
        try:
            activity = Activity.objects.get(code=activity_code.strip().lower())
        except Activity.DoesNotExist:
            activity = None

        # retrieve matching persons
        persons = Person.objects.filter(activity=activity)

        # create a string containing persons' names
        persons_a = []
        for person in persons:
            persons_a.append(person.name)

        count = _(u"%s People.") % persons.__len__()
        people_str = u""
        people_str += _(u", ").join(persons_a)
        answer = _(u"%(count)s %(people)s") \
                 % {'count': count, 'people': people_str}

        message.respond(answer[:160])
        return True

    keyword.prefix = ['stat', _(u"stat")]

    @keyword('')
    def stats(self, message):
        ''' returns the number of records in DB. '''

        persons = Person.objects.all()
        message.respond(_(u"Survey database knows about %d persons.") \
                        % persons.__len__())
        return True
