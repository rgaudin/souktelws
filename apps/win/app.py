!/usr/bin/env python
# encoding=utf-8

import rapidsms
from rapidsms.parsers.keyworder import Keyworder

from models import Player, Game, Participation, Question

class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            self.log("WIN: Pattern not found")
            return False

        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond("Error in WIN: %s" % e)
            return True

    keyword.prefix = ['start']

    @keyword('(\w+)')
    def win(self, message, game_code):
        ''' User starts a game '''

        try:
            game = Game.objects.get(code=game_code.lower(), \
                                    status=Game.STATUS_OPEN)
        except:
            message.respond(u"This Game is not registered or is closed!")
            return True

        try:
            player = Player.objects.get(backend=message.connection.backend, \
                                    identity=message.peer)        
        except Player.DoesNotExists:
            player = Player(backend=message.connection.backend, \
                                    identity=message.peer)
            player.save()

        message.respond()
