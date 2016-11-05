
from inventory import Inventory

class GameObject(object):
	def __init__(self, name, spaces=None):
		self.name = name
		self.spaces = {}
		if spaces:
			for space in spaces:
				self.addSpace(space)
		
	def addSpace(self, space):
		self.spaces[space] = Inventory()
		
	def getSpaces(self):
		return list(self.spaces.keys())
		
	def getSpace(self, prep):
		return self.spaces[prep]