import unittest

from item import Item
from location import Location
from gameObject import GameObject
from nounPhrase.noun import Noun

class LocationTest(unittest.TestCase):

	def test_identify_oneObject(self):
		location = Location("Name", "Description", 1)

		# Add a table to the room
		table = GameObject(Noun("Table"), spaces=["on"])
		location.addObject(table)

		# Add a "Thing" on the table
		thing = Item(Noun("thing"))
		table.getSpace("on").add(thing)

		# Method under test
		objectPaths = location.identify("thing")

		self.assertEqual(1, len(objectPaths))

		(foundObject, foundPath) = objectPaths[0]
		self.assertEqual(table, foundObject)
		self.assertEqual(1, len(foundPath))
		self.assertEqual([thing], foundPath["on"])
		
	def test_identify_oneObject_twoItems(self):
		location = Location("Name", "Description", 1)

		# Add a table to the room
		table = GameObject(Noun("Table"), spaces=["on"])
		location.addObject(table)

		# Add two "Things" on the table
		thing1 = Item(Noun("thing"))
		table.getSpace("on").add(thing1)
		thing2 = Item(Noun("thing"))
		table.getSpace("on").add(thing2)

		# Method under test
		objectPaths = location.identify("thing")

		self.assertEqual(1, len(objectPaths))

		(foundObject, foundPath) = objectPaths[0]
		self.assertEqual(table, foundObject)
		self.assertEqual(1, len(foundPath))
		self.assertEqual(2, len(foundPath["on"]))
		self.assertEqual(set([thing1, thing2]), set(foundPath["on"]))

if __name__ == '__main__':
    unittest.main()