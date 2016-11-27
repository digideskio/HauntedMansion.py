
class Inventory(object):
	def __init__(self):
		self.items = []
		self.itemsByName = {}
		
	def add(self, item):
		itemName = item.name.toString()
				
		# initialize an entry if not present
		if not itemName in self.itemsByName.keys():
			self.itemsByName[itemName] = []
			
		# add the item	
		items = self.itemsByName[itemName]
		items.append(item)
			
		self.items.append(item)
		
	def remove(self, item):
		self.items.remove(item)
		
		itemName = item.name.toString()
		items = self.itemsByName[itemName]
		items.remove(item)
		if len(items) == 0:
			del self.itemsByName[itemName]

	def contains(self, item):
		return self.items.contains(item)
				
	# return a list of items in this inventory that can be identified by the given name
	def identify(self, name):
		return [item for item in self.items if item.isIdentifiedBy(name)]