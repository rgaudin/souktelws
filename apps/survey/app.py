#!/usr/bin/env python
# encoding=utf-8

import rapidsms
from rapidsms.parsers.keyworder import Keyworder

from models import *


class App(rapidsms.app.App):

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
            message.respond(u"Survey System Error: %s" % e)
            return True

    keyword.prefix = ['help']

    @keyword('')
    def help(self, message):
        ''' display a usage message for the survey '''
        message.respond(u"Survey format: survey FIRST LAST SEX AGE (ACTIVITY)")
        return True

    keyword.prefix = ['survey', 'fill']

    @keyword(r'(\w+) (\w+) ([m|f]) (\d+)\s?(\w*)')
    def fill(self, message, first, last, sex, age, activity_code):
        ''' Enters a survey item into the DB '''

        # parse appropriate sex type
        if sex.lower() == 'm':
            sex = Person.MALE
        else:
            sex = Person.FEMALE

        # convert age to int
        age = int(age)

        # retrieve activity
        try:
            activity = Activity.objects.get(code=activity_code.strip().lower())
        except Activity.DoesNotExist:
            activity = None

        # create person object then save it.
        person = Person(first_name=first, last_name=last, sex=sex, \
                        age=age, activity=activity)
        person.save()

        message.respond(u"Thank you %(name)s for taking the survey. " \
                        "Your ID is %(id)s" \
                        % {'name': person.name, 'id': person.id})
        return True

    keyword.prefix = ''

    @keyword('find\s?(\w*)')
    def search(self, message, activity_code):
        ''' find the result of people in DB filtered by activity '''

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

        answer = u"%s People. " % persons.__len__()
        answer += u", ".join(persons_a)

        message.respond(answer[:160])
        return True

    keyword.prefix = ['stat', 'stats']

    @keyword('')
    def stats(self, message):
        ''' returns the number of records in DB. '''
        persons = Person.objects.all()
        message.respond(u"Survey database knows about %d persons." \
                        % persons.__len__())
        return True
