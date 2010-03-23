#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import rapidsms

class App(rapidsms.app.App):

    def handle(self, message):

        if message.text.lower().startswith('renaud'):
            message.respond(u"Hello %s" % message.text)
            return True

        return False
