import rapidsms

class App(rapidssms.app.App):
	
	def handle(self,message):
		
		message.response('ok')
		
		return False