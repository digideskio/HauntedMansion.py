
class Inventory(object):
	def __init__(self):
		self.items = []
		
	def add(self, item):
		self.items.append(item)
		
	def remove(self, item):
		self.items.remove(item)