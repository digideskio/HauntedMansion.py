
class Item(object):
	def __init__(self, name):
		self.name = name
		
	def identifiedBy(self, name):
		return self.name.identifiedBy(name)