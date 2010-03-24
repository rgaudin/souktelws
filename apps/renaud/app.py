#!usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

import rapidsms
from rapidsms.parsers.keyworder import Keyworder

class App(rapidsms.app.App):

    keyword = Keyworder()

    def handle(self, message):

        try:
            func, captures = self.keyword.match(self, message.text)
        except TypeError:
            #message.respond(u"Unrecognised message")
            return False
        try:
            return func(self, message, *captures)
        except Exception, e:
            message.respond(u"System encountered an Error: %s" % e)
            return True

    def old_handle(self, message):
        ''' not used anymore '''
        if message.text.lower().startswith('renaud'):
            message.respond(u"Hello %s" % message.text)
            return True

        return False

    keyword.prefix = ['renaud']
    @keyword(r'(\w+) ([y|n])')
    def renaud(self, message, text, exist):
        if exist == 'y':
            message.respond(u"Yes, %s exists." % text)
        else:
            message.respond(u"Sorry, %s doesn't exist." % text)
        return True

    keyword.prefix = ['product','multiply']
    @keyword(r'(\d+) (\d+)')
    def multiplication(self, message, first, second):
        first = int(first)
        second = int(second)
        result = first * second

        message.respond(u"%(first)s * %(second)s = %(res)s" % {'first': first, 'second': second, 'res': result})
        return True

