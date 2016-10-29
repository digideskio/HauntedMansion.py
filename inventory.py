
class Inventory(object):
	def __init__(self):
		self.items = []
		
	def add(self, item):
		self.items.append(item)
		
	def remove(self, item):
		self.items.remove(item)
				
	# return a list of items in this inventory that can be identified by the given name
	def identify(self, name):
		return [item for item in self.items if item.identifiedBy(name)]