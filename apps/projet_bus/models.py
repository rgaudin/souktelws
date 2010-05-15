#/usr/bin/env python
# encoding=utf-8

from django.db import models

class Ligne(models.Model):

    nomLigne= models.CharField(max_length=50)
    def __unicode__(self):
        return self.nomLigne

class Arret(models.Model):

    nomArret = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nomArret

class LigneArret(models.Model):

    nomLigne= models.CharField(max_length=50)
    nomArret = models.CharField(max_length=50)
    ordre = models.IntegerField(max_length=2, unique=False)

    def __unicode__(self):
        return u"%(nomLigne)s %(nomArret)s %(ordre)d" % {'nomLigne': self.nomLigne.title(), \
                                                     'nomArret': self.nomArret.title(), \
                                                     'ordre': self.ordre }

