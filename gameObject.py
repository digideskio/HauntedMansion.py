
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

	def removeItem(self, item, space):
		self.spaces[space].remove(item)

	def identify(self, name):
		paths = {};
		for space in self.spaces.keys():
			itemsInSpace = self.spaces[space].identify(name)
			if itemsInSpace:
				paths[space] = itemsInSpace

		return paths
