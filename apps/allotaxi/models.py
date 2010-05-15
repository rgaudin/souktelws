# encoding=utf-8

from django.db import models


#creation de la classe course

class Course(models.Model):

    
    
    date = models.DateTimeField ( auto_now_add=True)
    depart = models.ForeignKey("Lieu", related_name='depart')
    destination = models.ForeignKey("Lieu", related_name='destination')
    prix = models.PositiveIntegerField(blank=True,null=True)
    client = models.ForeignKey('Client')
    date_fin = models.DateTimeField(null=True,blank=True)
    taxi = models.ForeignKey('Taxi')
    
    def __unicode__(self):
        return u"hello"
        
class Taxi(models.Model):
    position = models.ForeignKey("Lieu")
    disponible = models.BooleanField()
    nom = models.CharField(max_length=30)
    numero = models.CharField(max_length=20)
    def __unicode__(self):
        return u"%s (%s)" % (self.nom, self.position)

class Client (models.Model):
    numero =   models.CharField(max_length=20, unique=True)
    def __unicode__(self):
        return u"%s" % (self.numero)

       
class Lieu (models.Model):
    class Meta:
        verbose_name = u"Lieu"
        verbose_name_plural = u"Lieux" 

    nom =   models.CharField(max_length=60)
    parent = models.ForeignKey("Lieu", null=True, blank=True)
    code = models.CharField(max_length=15, unique=True)
                        
    def __unicode__(self):
        if self.parent:
            return u"%s (%s)" % (self.nom, self.parent )
        else:
            return self.nom