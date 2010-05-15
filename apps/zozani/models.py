#/usr/bin/env python
# encoding=utf-8

from django.db import models

# je declare ma classe player
class Player(models.Model) : 
    
    first_name = models.CharField(max_length=30, verbose_name= "Nom")
    last_name = models.CharField(max_length=30, verbose_name= "Prenom")
    number = models.CharField(max_length=30, verbose_name= "Telephone")

    def __unicode__(self):
        return u"%(first)s %(last)s" % {'first': self.first_name.title(), \
                                       'last': self.last_name.title()}

