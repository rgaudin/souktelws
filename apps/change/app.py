#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
# maintainer: rgaudin

import rapidsms
from models import Currency

class App(rapidsms.app.App):

    def handle(self, message):
        ''' converts amount into desired courrency

        syntax: CHANGE CODE AMOUNT '''

        keyword, curr, amount = message.text.split(" ", 2)

        if keyword.lower() == 'change':
            
            currency = Currency.objects.get(code=curr.lower())
            
            new_rate = float(amount) * float(currency.rate)

            message.respond(u"%(msg)s ILS = %(new)s USD" % {'msg': amount, 'new': round(new_rate, 2)})

        return True
