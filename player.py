
from inventory import Inventory

class Player(object):
	def __init__(self):
		self.inventory = Inventory()
		self.weapon = None