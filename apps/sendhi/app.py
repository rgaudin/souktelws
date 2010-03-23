import rapidsms

class App(rapidsms.app.App):

    def handle(self, message):
        keyword = message.text

        if keyword.lower() == 'hi':
            message.respond(u"you have send %(msg)s" % {'msg': keyword})
            return True