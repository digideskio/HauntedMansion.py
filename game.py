import mapGen
import formatting
from name.indefiniteName import IndefiniteName
from name.adjective import Adjective
from name.noun import Noun
from item import Item
from player import Player
from colorama import Fore, Back, Style

class Game(object):
	def __init__(self):
		print("[creating a new game]")
		(maze, starting) = mapGen.createMaze(10, 10)
		self.playerLocation = starting
		self.player = Player()
		self.player.weapon = Item(IndefiniteName(Adjective("rusty", Noun("dagger"))))
		
	def look(self):
		print(formatting.title(self.playerLocation.name))
		print(self.playerLocation.description)
		print()
		
		# Show items
		if self.playerLocation.inventory.items:
			itemNames = formatting.itemNames(self.playerLocation.inventory.items)
			print("The room contains " + formatting.oxfordComma(itemNames) + ".")
		
		# Show valid moves
		doors = [formatting.door(door) for door in list(self.playerLocation.getDoors())]
		if not doors:
			print("There is nowhere to go.")
		else:
			print("You can go " + formatting.oxfordComma(doors) + ".")
			
	def inventory(self):
		itemNames = formatting.itemNames(self.player.inventory.items)
	
		if not self.player.weapon:
			if not self.player.inventory.items:
				print("You are unarmed and carry nothing.")
			else:
				print("You are unarmed.")
				print("You carry " + formatting.oxfordComma(itemNames) + ".")
		else:
			weaponStr = "You are armed with " + formatting.itemName(self.player.weapon.name.getDeclarative())
			if not self.player.inventory.items:
				print(weaponStr + ", and carry no other items.")
			else:
				print(weaponStr + ".")
				print("You carry " + formatting.oxfordComma(itemNames) + ".")
				
	def get(self, name):
		validItems = self.playerLocation.inventory.identify(name)
		if (validItems):
			itemToGet = validItems[0]
			self.playerLocation.inventory.remove(itemToGet)
			self.player.inventory.add(itemToGet)
			print("You collect " + formatting.itemName(itemToGet.name.simplify().getDefinite()) + ".")
		else:
			print("There is nothing here called \"" + name + "\".")
			
	def movePlayer(self, door):
		if not self.playerLocation.hasDoor(door):
			print("You cannot go that way.")
		else:
			print("You go " + formatting.door(door) + "...")
			print()
			self.playerLocation = self.playerLocation.getDoor(door)
			self.look()		