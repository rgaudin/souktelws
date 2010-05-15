#/usr/bin/env python
# encoding=utf-8

import rapidsms
import random

from django.db import IntegrityError


from rapidsms.parsers.keyworder import Keyworder

from models import Player

class App(rapidsms.app.App):
    
    keyword = Keyworder()
    
    def handle(self, message):
        ''' cette methode s'execute si le router recoit un sms '''
        # on essaye de recuperer la reference de la fonction dans func a partir du paterne et
        # dans captures les valeurs dont on a besoin dans le sms
        try:
            func, captures = self.keyword.match(self, message.text)
        # s'execute si le format du sms n'est pas bon
        except TypeError:
            message.respond("format inconnu")
            return False
        # on essaye de retourner la fonction avec comme parametre le sms, les captures
        try:
            return func(self, message, *captures)
        # s'execute si la fonction concernée leve une exception
        except Exception, e:
            message.respond("Erreur: %s" % e)
            return True
    # verifie le format de sms avant d'excuter la fonction qui suit
    @keyword(r'player (\w+) (\w+)')    
    def player(self, message, first, last):
        ''' format sms: player first last
        
        la fonction repond une phrase au hasard a un player '''
        # creation d'un player 
        player = Player(first_name=first, \
                                last_name=last, \
                                
                                number=message.peer)
                                
        # ma liste de reponse 
        list= ["vous etes un as", 
                "vous etes formidable",
                "reesayez vous pouvez le faire", 
                'vive le SENEGAL',
                u"vous n'etes pas trop doué",
                "vous êtes un pythonier"]
        # je melange ma liste et je tire une phrase au hasard
        ran = random.choice(list)
        
        # renvoie d'une reponse        
        message.respond(u"%(att)s, %(att1)s." % {'att': player, 'att1':ran})
        # sauvegarde le player
        player.save()

        return True
