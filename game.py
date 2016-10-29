import mapGen
import formatting
from name.indefiniteName import IndefiniteName
from name.adjective import Adjective
from name.noun import Noun
from item import Item
from player import Player

class Game(object):
	def __init__(self):
		print("[creating a new game]")
		(maze, starting) = mapGen.createMaze(10, 10)
		self.playerLocation = starting
		self.player = Player()
		self.player.weapon = Item(IndefiniteName(Adjective("rusty", Noun("dagger"))))
		
	def look(self):
		print(self.playerLocation.name)
		print(self.playerLocation.description)
		print()
		
		# Show items
		if self.playerLocation.inventory.items:
			itemNames = [item.name.getDeclarative() for item in self.playerLocation.inventory.items]
			print("The room contains " + formatting.oxfordComma(itemNames) + ".")
		
		# Show valid moves
		doors = list(self.playerLocation.getDoors())
		if not doors:
			print("There is nowhere to go.")
		else:
			print("You can go " + formatting.oxfordComma(doors) + ".")
			
	def inventory(self):
		itemNames = [item.name.getDeclarative() for item in self.player.inventory.items]
	
		if not self.player.weapon:
			if not self.player.inventory.items:
				print("You are unarmed and carry nothing.")
			else:
				print("You are unarmed.")
				print("You carry " + formatting.oxfordComma(itemNames) + ".")
		else:
			weaponStr = "You are armed with " + self.player.weapon.name.getDeclarative()
			if not self.player.inventory.items:
				print(weaponStr + ", and carry no other items.")
			else:
				print(weaponStr + ".")
				print("You carry " + formatting.oxfordComma(itemNames) + ".")
			
	def movePlayer(self, door):
		if not self.playerLocation.hasDoor(door):
			print("You cannot go that way.")
		else:
			print("You go " + door + "...")
			print()
			self.playerLocation = self.playerLocation.getDoor(door)
			self.look()		