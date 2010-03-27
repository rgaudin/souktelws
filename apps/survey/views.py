#/usr/bin/env python
# encoding=utf-8

''' Survey App Views

- Dashboard lists some statistics and list of persons
- Person Profile detailed view '''

from django.http import HttpResponse
from rapidsms.webui.utils import render_to_response
from django.contrib.auth.decorators import login_required

from models import *

def index(request):
    ''' Displays a Dashboard

    List last 5 encounters
    Displays percentage by sex and activity '''

    # list of 5 last encounters
    persons = Person.objects.all().order_by('-entered_on')

    # male/female percentages
    total = persons.count()
    male = persons.filter(sex=Person.MALE).count() * 100 / total

    # activities breakdown
    activities = Activity.objects.all()
    activities_pc = []
    for activity in activities:
        percent = activity.person_set.count() * 100 / total
        activities_pc.append({'activity': activity, 'pc': percent})
    

    return render_to_response(request, 'survey/index.html', \
            {'persons': persons[:5],
             'percent': {'male': male, 'female': 100 - male},
             'total': total,
             'activities_pc': activities_pc,
            })

def person_detail(request, userid):
    ''' Displays one person's complete profile '''

    person = Person.objects.get(id=userid)
    return render_to_response(request, 'survey/person.html', \
            {'person': person})
