
from django.contrib import admin
from models import *

class TaxiAdmin(admin.ModelAdmin):

    list_display = ('nom','disponible','numero')
    list_filter = ('disponible',)

class LieuAdmin(admin.ModelAdmin):
    list_display = ('nom','code', 'parent')
    list_filter=('parent',)

class CourseAdmin(admin.ModelAdmin):
    list_display=('taxi','date','depart','destination','date_fin','prix')
    list_filter=('taxi','depart','destination')

admin.site.register(Course, CourseAdmin)
admin.site.register(Client)
admin.site.register(Lieu, LieuAdmin)
admin.site.register(Taxi, TaxiAdmin)
