import unittest

from item import Item
from gameObject import GameObject
from nounPhrase.noun import Noun

class InventoryTest(unittest.TestCase):

	def test_empty(self):
		object = GameObject(Noun("table"))
		self.assertFalse(object.getSpaces())
		
	def test_spaces(self):
		object = GameObject(Noun("table"), spaces=["on"])
		self.assertEquals(1, len(object.getSpaces()))
		self.assertIn("on", object.getSpaces())

	def test_identify_simple(self):
		object = GameObject(Noun("table"), spaces=["on"])
		onTable = object.getSpace("on")
		thingOnTable = Item(Noun("thing"))
		onTable.add(thingOnTable)

		# the method under test
		itemPaths = object.identify("thing")
		
		self.assertEquals(1, len(itemPaths))
		self.assertEquals(["on"], list(itemPaths.keys()))
		self.assertIn(thingOnTable, itemPaths["on"])
		
	def test_identify_none(self):
		object = GameObject(Noun("table"), spaces=["on"])
		onTable = object.getSpace("on")
		thingOnTable = Item(Noun("thing"))
		onTable.add(thingOnTable)

		# the method under test
		itemPaths = object.identify("invalid")
		
		self.assertEquals(0, len(itemPaths))

	def test_identify_multipleSpaces(self):
		object = GameObject(Noun("table"), spaces=["on", "under"])

		# Add a "thing" on the table
		onTable = object.getSpace("on")
		thingOnTable = Item(Noun("thing"))
		onTable.add(thingOnTable)

		# Add a "thing" under the table
		underTable = object.getSpace("under")
		thingUnderTable = Item(Noun("thing"))
		underTable.add(thingUnderTable)

		# the method under test
		itemPaths = object.identify("thing")
		
		self.assertEquals(2, len(itemPaths))
		self.assertEquals(set(["on", "under"]), set(itemPaths.keys()))
		self.assertIn(thingOnTable, itemPaths["on"])
		self.assertIn(thingUnderTable, itemPaths["under"])
		
if __name__ == '__main__':
    unittest.main()