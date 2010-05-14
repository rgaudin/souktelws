#!/usr/bin/env python
# encoding=utf-8

from django.db import models

class Game(models.Model):
    ''' A game is a set of questions and parameters. '''

    STATUS_OPEN = 0
    STATUS_CLOSED = 1

    STATUSES = (
        (STATUS_OPEN, u"Open"),
        (STATUS_CLOSED, u"Closed"),
    )

    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUSES, \
                              default=STATUS_CLOSED)
    questions = models.ManyToManyField('Question', blank=True)
    max_winners = models.PositiveIntegerField(default=10, blank=True, null=True)
    max_failed_attempts = models.PositiveIntegerField(default=3, blank=True, null=True)
    winners = models.ManyToManyField('Player', blank=True, null=True)

    def __unicode__(self):
        return u"%(name)s (%(status)s)" \
               % {'name': self.name, 'status': self.status_name}

    @property
    def status_name(self):
        ''' returns the human-readable version of status '''
        for value, name in self.STATUSES:
            if value == int(self.status):
                return name
        return self.status

    def next_question(self, player):
        ''' returns next question for a player '''

        last_parts = Participation.objects.filter(player=player, game=self).order_by('-date')[:1]
        if last_parts.__len__():
            # if waiting
            waitings = last_parts.filter(status__in=(Participation.STATUS_WAITING, Participation.STATUS_FAILED))
            if waitings.__len__():
                return waitings[0].question
            else:
            # get next level
            
        else:
            # create new            
            

class Player(models.Model):
    ''' Player is phone number person '''

    backend = models.CharField(max_length=50)
    identity = models.CharField(max_length=50)

    def __unicode__(self):
        return self.identity

    def failed_attempts(self, game=None):
        parts = Participation.objects.filter(player=self, \
                                            status=Participation.STATUS_FAILED)
        if game:
            return parts.filter(game=game).count()
        else:
            return parts.count()

class Question(models.Model):
    ''' Question/Answer couple '''

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return u"L%(level)d: %(quest)s" \
               % {'quest': self.question, 'level': self.level}

class Participation(models.Model):
    ''' Participation records one answering a question in a game '''

    STATUS_WAITING = 0
    STATUS_FAILED = 1
    STATUS_SUCCESS = 2

    STATUSES = (
        (STATUS_WAITING, u"Waiting"),
        (STATUS_FAILED, u"Failed"),
        (STATUS_SUCCESS, u"Success"),
    )

    game = models.ForeignKey('Game')
    player = models.ForeignKey('Player')
    date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question')
    status = models.CharField(max_length=1, choices=STATUSES, \
                              default=STATUS_WAITING)

    def __unicode__(self):
        return u"%(player)s %(status)s on %(game)s at %(date)s" \
               % {'player': self.player, 'date': self.date.strftime("%w"), \
                  'status': self.status_name, 'game': self.game}

    @property
    def status_name(self):
        ''' returns the human-readable version of status '''
        for value, name in self.STATUSES:
            if value == int(self.status):
                return name
        return self.status
    
