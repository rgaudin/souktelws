#!/usr/bin/env python
#vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin

import rapidsms
import datetime
from calendar import weekday
from models import Weather, WeatherLocation, WeatherSky

class App(rapidsms.app.App):

       def handle(self, message):
		''' converts amount into desired courrency

		syntax: CHANGE CODE AMOUNT '''

                self.daytoday = {
                            0: {'id': 'mon', 'ar': u"الأثنين"},
                            1: {'id': 'tue', 'ar': u"الثلاثاء"},
                            2: {'id': 'wed', 'ar': u"الأربعاء"},
                            3: {'id': 'thu', 'ar': u"الخميس"},
                            4: {'id': 'fri', 'ar': u"الجمعة"},
                            5: {'id': 'sat', 'ar': u"السبت"},
                            6: {'id': 'sun', 'ar': u"الاحد"}
                            }

                if not message.text.startswith('weather'):
                    return False

                try:
                    keyword , parameters = message.text.split(" ", 1)
                except:
                    message.respond(u"خطأ في سياق حالة الجو  [day]")
                    return True


                param_split = parameters.split(" ", 1)

                
                if param_split.__len__() == 1:
                    country = param_split[0]
                    today = self.daytoday[datetime.datetime.now().weekday()]['id']

                elif param_split.__len__() == 2:
                    country = param_split[0]
                    today = param_split[1].lower()

                if today not in ('mon','tue','wed','thu','fri','sat', 'sun'):
                    message.respond("اليوم المدخل غير صحيح  Mon, Tue, etc.")
                    return True

                country_code = country.strip().lower()

                try:
                    location = WeatherLocation.objects.get(code=country_code)
                except:
                    message.respond(u"المنطقة المحددة غير موجودة الرجاء إدخال الرمز الصحيح ")
                    return True
        	weather = Weather.objects.get(weatherLocation=location,dayofweek=today)

                day_string = self.name_from_id(today)
		message.respond(u"يكون الجو  في مدينة %(name)s يوم  %(sky)s %(day)s و درجة الحرارة %(temp)s" % {'name':location.name, 'sky':weather.sky.name, 'temp': weather.temp, 'day': day_string})
                return True

       def name_from_id(self, id):
                for index in self.daytoday:
                    if self.daytoday[index]['id'] == id:
                        return self.daytoday[index]['ar']
                return self.daytoday[0]['ar']