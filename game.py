import mapGen
import formatting
from nounPhrase.adjective import Adjective
from nounPhrase.noun import Noun
from nounPhrase.alwaysDefinite import AlwaysDefinite
from item import Item
from player import Player
from colorama import Fore, Back, Style

class Game(object):
	def __init__(self):
		print("[creating a new game]")
		(maze, starting) = mapGen.createMaze(10, 10)
		self.playerLocation = starting
		
		# Initalize the player and starting items
		self.player = Player()
		self.player.weapon = Item(Adjective("rusty", Noun("dagger")), isWeapon=True)
		mansionKey = Item(AlwaysDefinite(Adjective("mansion", Noun("key"))))
		self.player.inventory.add(mansionKey)
		
	def look(self):
		print(formatting.title(self.playerLocation.name))
		print(self.playerLocation.description)
		print()
		
		# Show items
		if self.playerLocation.inventory.items:
			itemNames = formatting.itemNamesIndefinite(self.playerLocation.inventory.items)
			print("The room contains " + formatting.oxfordComma(itemNames) + ".")
		
		# Show valid moves
		doors = [formatting.door(door) for door in list(self.playerLocation.getDoors())]
		if not doors:
			print("There is nowhere to go.")
		else:
			print("You can go " + formatting.oxfordComma(doors) + ".")
			
	def inventory(self):
		itemNames = formatting.itemNamesIndefinite(self.player.inventory.items)
		weapon = self.player.weapon
	
		if not weapon:
			if not self.player.inventory.items:
				print("You are unarmed and carry nothing.")
			else:
				print("You are unarmed.")
				print("You carry " + formatting.oxfordComma(itemNames) + ".")
		else:
			weaponStr = "You are armed with " + formatting.itemName(weapon, weapon.name.makeIndefinite())
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
			simpleItemName = itemToGet.name.stripAdjectives().makeDefinite()
			print("You collect " + formatting.itemName(itemToGet, simpleItemName) + ".")
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