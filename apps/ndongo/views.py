#/usr/bin/env python
# encoding=utf-8

import random

from rapidsms.webui.utils import render_to_response
from django.contrib.auth.decorators import login_required

from models import *

@login_required
def index(request):

    if request.method == 'POST':
        try:
            nb_winners = int(request.POST['nb_winners'])
        except ValueError:
            nb_winners = 0
    else:
        nb_winners = 0

    if nb_winners:
        # Group A & B
        groups = Group.objects.filter(name__in=('A','B'))

        # list of students from those groups
        students = Attendee.objects.filter(group__in=(groups))

        # random 10 students
        winners = random.sample(students, nb_winners)
    else:
        winners = None

    return render_to_response(request, 'index.html', {'winners': winners})


# [<Attendee: Mor Syll>, <Attendee: Joseph Ndaw>, <Attendee: Ndiaye Cheick_Amadou_Tidiane>, <Attendee: Mouhamed Sow>, <Attendee: Amadou Malamine>, <Attendee: Birame Diouf>, <Attendee: Sokhnakhadi Ndiaye>, <Attendee: Cheikh Kane>, <Attendee: Aida Ndiaye>, <Attendee: Seydou Ba>]
 

