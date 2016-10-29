
class Item(object):
	def __init__(self, name, isWeapon=False):
		self.name = name
		self.isWeapon = isWeapon
		
	def isIdentifiedBy(self, name):
		return self.name.isIdentifiedBy(name)