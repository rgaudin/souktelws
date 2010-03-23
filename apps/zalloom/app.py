#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
import rapidsms

class App(rapidsms.app.App):

    def handle(self, message):
	
		if message.text.startswith('Hello'):
			message.respond(u"Hello All")
	
		return True

