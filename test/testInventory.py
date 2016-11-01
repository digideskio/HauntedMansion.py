import unittest

from item import Item
from inventory import Inventory
from nounPhrase.noun import Noun

class InventoryTest(unittest.TestCase):

	def test_empty(self):
		inventory = Inventory()
		self.assertEquals(0, len(inventory.items))
	
	def test_add(self):
		inventory = Inventory()
		item = Item(Noun("foo"))
		inventory.add(item)
		self.assertIn(item, inventory.items)
		
	def test_remove(self):
		inventory = Inventory()
		item = Item(Noun("foo"))
		inventory.add(item)
		inventory.remove(item)
		self.assertNotIn(item, inventory.items)
		
	def test_identify(self):
		inventory = Inventory()
		item = Item(Noun("foo"))
		inventory.add(item)
		
		identified = inventory.identify("foo")
		self.assertEquals(1, len(identified))
		self.assertIn(item, identified)
		
	def test_identify_nonMatches(self):
		inventory = Inventory()
		item = Item(Noun("foo"))
		inventory.add(item)
		inventory.add(Item(Noun("bar")))
		inventory.add(Item(Noun("baz")))
		
		identified = inventory.identify("foo")
		self.assertEquals(1, len(identified))
		self.assertIn(item, identified)
		
	def test_identify_multipleMatches(self):
		inventory = Inventory()
		
		match = Item(Noun("foo"))
		inventory.add(match)
		otherMatch = Item(Noun("foo"))
		inventory.add(otherMatch)
		
		inventory.add(Item(Noun("bar")))
		
		identified = inventory.identify("foo")
		self.assertEquals(2, len(identified))
		self.assertIn(match, identified)
		self.assertIn(otherMatch, identified)
		
	def test_identify_noMatches(self):
		inventory = Inventory()
		item = Item(Noun("foo"))
		inventory.add(item)
		
		identified = inventory.identify("bar")
		self.assertEquals(0, len(identified))
		
if __name__ == '__main__':
    unittest.main()