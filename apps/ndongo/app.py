#/usr/bin/env python
# encoding=utf-8

import rapidsms
import random


from django.db import IntegrityError
from rapidsms.parsers.keyworder import Keyworder

from models import Attendee, Group


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

    @keyword(r'register (\w+) (\w+) ([a-z]*@[a-z]*\.[a-z]*)')    
    def register(self, message, first, last, email):
        ''' register first last email '''
        
        attendee = Attendee(first_name=first, \
                                last_name=last, \
                                email=email, \
                                number=message.peer)
        try:
            attendee.save()
        except IntegrityError:
            att2 = Attendee.objects.get(number=message.peer)
            message.respond("Desole, ce numero est deja enregistre " \
                            "pour %s" % att2)
            return True

        message.respond(u"Merci %(att)s. Vous etes bien enregistré." % {'att': attendee})

        return True

    @keyword(r'dispatch')
    def dispatch(self, message):

        if message.peer in ('+221772059418', '1111'):

            attendees = list(Attendee.objects.filter(group__isnull=True))
            
            random.shuffle(attendees)

            groupa = Group.objects.get(name='A')
            groupb = Group.objects.get(name='B')

            msg = "%(name)s, vous faites parti du groupe %(group)s"
            
            for attendee in attendees[::2]:
                attendee.group = groupa
                attendee.save()
                message.forward(attendee.number, msg % {'name': attendee, 'group': attendee.group})
                
            for attendee in attendees[1::2]:
                attendee.group = groupb
                attendee.save()
                message.forward(attendee.number, msg % {'name': attendee, 'group': attendee.group})
            
            message.respond("group formés pour %d personnes" % attendees.__len__())
            return True

        else:
            message.respond("desole, tu n'es pas autorise a faire ca")
            return True



