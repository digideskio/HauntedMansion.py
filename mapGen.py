from location import Location
import random
import mazeGen
from item import Item
from nounPhrase.adjective import Adjective
from nounPhrase.noun import Noun
from nounPhrase.preposition import Preposition

#######################
# Item Generators
#
# These tuples include the minimum/maximum opulence the item should be generated for,
# and a function for generating the item.
#######################
itemGenerators = [
	# Rubbish items
	(0, 1, lambda: Item(Adjective("dead", Noun("mouse", irregularPlural="mice")))),
	(0, 2, lambda: Item(Adjective("broken", Noun("cup")))),
	(0, 2, lambda: Item(Adjective("empty", Noun("sack")))),
	(1, 2, lambda: Item(Noun("potato"))),

	# functional items
	(0, 10, lambda: Item(Noun("key"))),
	
	# Victorian items
	(3, 6, lambda: Item(Adjective("wooden", Noun("candlestick")))),
	(3, 6, lambda: Item(Adjective("herbal", Noun("remedy"), hasVowelSound=True))),
	(2, 7, lambda: Item(Adjective("empty", Preposition(Noun("phial"), "of mercury")))),
	(3, 7, lambda: Item(Preposition(Noun("phial"), "of mercury"))),
	(5, 10, lambda: Item(Adjective("cigar", Noun("box")))),
	(4, 8, lambda: Item(Adjective("world", Noun("atlas")))),
	(6, 10, lambda: Item(Adjective("silver", Adjective("snuff", Noun("box"))))),
	(8, 10, lambda: Item(Adjective("exquisite", Noun("candlestick")))),
	
	# weapons
	(1, 4, lambda: Item(Adjective("cheese", Noun("knife")), isWeapon=True)),
	(5, 8, lambda: Item(Adjective("silver", Noun("dagger")), isWeapon=True)),
	(10, 10, lambda: Item(Adjective("antique", Noun("sabre")), isWeapon=True))
]

roomTitles = [
		# Very opulent rooms
		("Decorated Hallway", 8, 10),
		("Master Bedroom", 9, 10),
		("Grand Ballroom", 8, 10),
		("Private Study", 8, 10),
		("Fine Washroom", 8, 10),
		
		# Opulent rooms
		("Guest Bedroom", 6, 8),
		("Study", 6, 8),
		("Drawing Room", 5, 8),
		("Dining Room", 5, 8),
		
		# Functional rooms
		("Water closet", 4, 6),
		("Conservatory", 4, 6),
		("Halway", 3, 6),
		("Pantry", 3, 4),
		
		# Dismal rooms
		("Servants' Quarters", 2, 4),
		("Kitchen", 2, 4),
		("Narrow Corridor", 1, 3),
		("Dank Cell", 0, 2),
]

roomDecor = [
	"Ancient bas-reliefs depict scenes of treachery and descruction.",
	"The unintelligible writings of some hasty hand plaster the walls.",
	"Once-fine wood carvings have long turned to dust."
]

def createMaze(width, height):
	(maze, startingCell) = mazeGen.randomizedPrim(width, height)
	print("...generating mansion rooms")
	
	# initialize the locations
	rooms = []
	for row in range(0, height):
		roomsRow = []
		rooms.append(roomsRow)
		for col in range(0, width):
			mazeCell = maze[row][col]
			location = makeLocation(mazeCell)
			roomsRow.append(location)
			
	# connect the doors based on the generated maze
	for row in range(0, height):
		for col in range(0, width):
			sourceLoc = rooms[row][col]
			mazeCell = maze[row][col]
			for door in mazeCell.doors:
				(destRow, destCol) = door.dest
				destLoc = rooms[destRow][destCol]
				sourceLoc.addDoor(door.direction, destLoc)
	
	(startRow, startCol) = startingCell.position
	startingLocation = rooms[startRow][startCol]
	return (rooms, startingLocation)
	
def makeLocation(mazeCell):
	opulence = min(10, mazeCell.distance)
	validTitles = [title for (title, min, max) in roomTitles if min <= opulence <= max]
	title = random.choice(validTitles)
	
	description = random.choice(roomDecor)
	description += " " + random.choice(roomDecor)
	
	location = Location(title, description, mazeCell.distance)
	
	if random.random() > 0.25:
		numItems = random.randint(1, 4)
		validItemGenerators = [gen for (min, max, gen) in itemGenerators if min <= opulence <= max]
		for i in range(numItems):
			makeItem = random.choice(validItemGenerators)
			item = makeItem()
			location.inventory.add(item)
	
	return location
	
def connect(locationA, locationB, direction, inverse):
	locationA.addDoor(direction, locationB)
	locationB.addDoor(inverse, locationA)