class Uri:
	def __init__(self,name,uri):
		self.link = uri
		self.name = name

def get_base_values(request):
	return {'uris':[Uri("Home","/index"),Uri("Base","/")]}
	
	
