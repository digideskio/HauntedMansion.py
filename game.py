import mapGen
import formatting
from nounPhrase.adjective import Adjective
from nounPhrase.noun import Noun
from nounPhrase.alwaysDefinite import AlwaysDefinite
from nounPhrase.preposition import Preposition
from item import Item
from player import Player

class Game(object):
	def __init__(self):
		print("...creating a new game")
		(maze, starting) = mapGen.createMaze(8, 8)
		self.playerLocation = starting
				
		# Initalize the player and starting items
		self.player = Player()
		self.player.weapon = Item(Adjective("rusty", Noun("dagger")), isWeapon=True)
		mansionKey = Item(AlwaysDefinite(Adjective("mansion", Noun("key"))))
		mansionKey = Item(AlwaysDefinite(Preposition(Noun("key"), "to the mansion")))
		self.player.inventory.add(mansionKey)
		
	def look(self):
		location = self.playerLocation
	
		print(formatting.title(self.playerLocation.name))
		print(self.playerLocation.description)
		print()
		
		# Show objects
		if location.objects:
			for object in location.objects:
				desc = "You see " + formatting.roomFeatureName(object, object.name.makeIndefinite()) + "."
				spaces = object.getSpaces()
				if spaces:
					for space in spaces:
						itemNames = formatting.inventoryItems(object.getSpace(space))
						desc += " " + space.capitalize() + " it you see " + formatting.oxfordComma(itemNames) + "."
				print(desc)
			print()
		
		# Show valid moves
		doors = [formatting.door(door) for door in list(location.getDoors())]
		if not doors:
			print("There is nowhere to go.")
		else:
			print("You can go " + formatting.oxfordComma(doors) + ".")
			
	def inventory(self):
		itemNames = formatting.inventoryItems(self.player.inventory)
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
		None
			
	def movePlayer(self, door):
		if not self.playerLocation.hasDoor(door):
			doors = [formatting.door(door) for door in list(self.playerLocation.getDoors())]
			print("You cannot go that way. You can go " + formatting.oxfordComma(doors, conjunction="or") + ".")
		else:
			print("You go " + formatting.door(door) + "...")
			print()
			self.playerLocation = self.playerLocation.getDoor(door)
			self.look()		