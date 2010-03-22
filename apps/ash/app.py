# encoding=utf-8

import rapidsms
import time
import re
from models import worldClock
import math 

class App(rapidsms.app.App):
	
	def handle(self,message):
		
		#cities = { 'jeruslem':2, 'paris':1 , 'london':2 ,'nyc':3,'utc+2':0}
		
		if not message.text.startswith('time ') : 
			message.respond(u"لم يتم العثور على الامر ")
			
			
		parsing = re.split("\s+", message.text.lower())
		
		if parsing.__len__()  <> 2 :
			message.respond(u"يوجد خطا في صيغة الامر , الرجاء ادخال اسم الامر متبوعا بـ اسم المدينة")
			return True
 
 
		keyword , city_code = parsing 
 
			
		try:
			worldClk = worldClock.objects.get(code=city_code )
		except:
			message.respond(u"رمز المدينة :(%s) غير موجود !" %  city_code)
			return True
			
		worldClk = worldClock.objects.get(code=city_code )
		location = worldClk.cityName 
		deff =worldClk.diff
		#deffHour =  deff[0] 
		#defMin = float( '0.'+deff[1] )  * 60
 
		newTime =   u"%(h)s:%(m)s:%(ss)s" %  {'h': int(time.gmtime()[3]  +  deff) ,  'm': time.gmtime()[4] , 'ss': time.gmtime()[5]}
		message.respond(u"الوقت الحالي لمدينة  %s هو : %s " % (  location , newTime ) ) 
		    
		return True
		
 
