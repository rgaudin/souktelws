#/usr/bin/env python
# encoding=utf-8

import rapidsms
import random


from django.db import IntegrityError
from rapidsms.parsers.keyworder import Keyworder

from models import LigneArret


class App(rapidsms.app.App):
    
    keyword = Keyworder()

    def handle(self, message):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            message.respond("format inconnu")
            return False

        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond("Erreur: %s" % e)
            return True

    #@keyword(r'bus ([a-z\s]+),([a-z\s]+)')
    @keyword(r'bus (\w+) (\w+)')    
    def bus(self, message, depart, arrive):
        #mess2=message.text.lower().split(",")
        #depart1=mess2[0
        
        mess = ""
        busDep = LigneArret.objects.filter(nomArret=depart.lower())
        busAr = LigneArret.objects.filter(nomArret=arrive.lower())

        for x in busDep:
            for y in busAr: 
                if x.nomLigne.lower() == y.nomLigne.lower():
                    mess = mess +' ' + x.nomLigne 
        if mess == "":
            message.respond("pas de lignes disponibles")
        else:
            message.respond("les lignes sont %s" % mess)
        return True



