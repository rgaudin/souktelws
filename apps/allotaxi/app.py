# encoding=utf-8

from rapidsms.parsers.keyworder import Keyworder
from models import *
import rapidsms
from datetime import datetime
class App(rapidsms.app.App):
    
    keyword = Keyworder()
    
    def handle(self, message):
        ''' finds out corresponding function and call it

        Use the Keyworder parser '''

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            self.log('INFO', u"Allo Taxi: not catched")
            return False

        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(u"Taxi System Error: %s" % e)
            return True

    @keyword('taxi (\w+) (\w+)')
    def appel(self, message, position, destination):
        ''' taxi position destination '''

        try:
            origine= Lieu.objects.get(code=position.lower())
        
            destinat= Lieu.objects.get(code=destination.lower())
        except Lieu.DoesNotExist:
               message.respond(u"Votre position  n' existe pas , desole veuillez envoyer : aide")
               return True 
        try:
            client = Client.objects.get(numero=message.peer)
        except Client.DoesNotExist:
        
            client = Client(numero=message.peer)
            client.save()

        # test si taxi dispo
        libres = Taxi.objects.filter(disponible=True)
        if libres.__len__():
            taxi = libres[0]        
            message.respond("vous avez demande un taxi de %s à %s , veuillez Patienter " % (origine ,destinat))
            message.forward(taxi.numero, "Vas vite a %s. Numero: %s." % (destinat, client.numero))
            taxi.disponible= False     
            taxi.save()
            course=Course(depart=origine,client=client,destination=destinat,taxi=taxi)
            course.save()
        else:
            message.respond("Desole, pas de taxi disponible pour le moment")
        return True
        # envoi desole
        # selection premier taxi libre
        
        # envoi sms taximan : position client, numero, compte
        
        # envoi sms client: on arrive
        
        # change statut taxi
        # cree la course
        
        
    @keyword('fin (\w+) (\d+)')
    def fin_course(self, message,position,prix):
        ''' fin position prix  '''
        try: 
            taxi = Taxi.objects.get(numero=message.peer)
        except Taxi.DoesNotExist:
            message.respond("vous n' etes autoriser a ce service")
            return True
        try:
            posit=Lieu.objects.get(code=position.lower())
            
        except Lieu.DoesNotExist:
            message.respond("la positiond indiquee n' existe pas,merci")
        
        course = Course.objects.get(taxi=taxi, date_fin__isnull=True)
        course.prix = int(prix)
        course.date_fin = datetime.now()
        course.save()
        taxi.disponible = True
        taxi.save()
        message.respond("merci, t'es gentil")
        

    @keyword('aide\s?(\w*)')
    def aide(self, message, position):
    
        try:
            
            parent= Lieu.objects.get(code=position.lower())
            liste = Lieu.objects.filter(parent=parent)
        except:
            liste = Lieu.objects.filter(parent=None)
        self.log('INFO', liste)
        self.log('INFO', position)
        liste_code = ["%s : %s" %( lieu.code, lieu.nom) for lieu in liste]
        l = " - ".join(liste_code)
        message.respond("Les liste disponible : %s" % l)
        
            
