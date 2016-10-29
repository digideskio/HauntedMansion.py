
class Item(object):
	def __init__(self, name):
		self.name = name
		
	def isIdentifiedBy(self, name):
		return self.name.isIdentifiedBy(name)