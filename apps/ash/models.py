from django.db import models 



class worldClock( models.Model ):
	
	cityName= models.CharField(max_length=30)
	diff = models.FloatField() # 1 -2 
	code = models.CharField(max_length=3)
	
	
	
	