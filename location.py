
from inventory import Inventory

class Location(object):
	def __init__(self, name, description, distance):
		self.name = name
		self.description = description
		self.doors = {}
		self.inventory = Inventory()
		self.distance = distance # distance from starting room
		
	def addDoor(self, direction, location):
		self.doors[direction] = location
		
	def hasDoor(self, direction):
		return self.doors.get(direction) is not None
		
	def getDoors(self):
		return self.doors.keys()
		
	def getDoor(self, direction):
		return self.doors.get(direction)