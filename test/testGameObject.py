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
		
if __name__ == '__main__':
    unittest.main()