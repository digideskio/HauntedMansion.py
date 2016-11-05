from location import Location
import random
import mazeGen
from item import Item
from nounPhrase.adjective import Adjective
from nounPhrase.noun import Noun
from nounPhrase.preposition import Preposition
from gameObject import GameObject

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
		(2, 7, lambda: Item(Adjective("empty", Adjective("mercury", Noun("phial"))))),
		(3, 7, lambda: Item(Preposition(Noun("phial"), "of mercury"))),
		(5, 10, lambda: Item(Adjective("cigar", Noun("box")))),
		(4, 8, lambda: Item(Adjective("world", Noun("atlas")))),
		(6, 10, lambda: Item(Adjective("silver", Adjective("snuff", Noun("box"))))),
		(8, 10, lambda: Item(Adjective("exquisite", Noun("candlestick")))),
	
		# weapons
		(1, 4, lambda: Item(Adjective("cheese", Noun("knife", irregularPlural="knives")), isWeapon=True)),
		(5, 8, lambda: Item(Adjective("silver", Noun("dagger")), isWeapon=True)),
		(10, 10, lambda: Item(Adjective("antique", Noun("sabre")), isWeapon=True))
]

#######################
# Object Generators
#
# These tuples include the minimum/maximum opulence the item should be generated for,
# and a function for generating the item.
#######################
objectGenerators = [
		(0, 1, lambda: GameObject(Preposition(Noun("pile"), "of straw"), spaces=["inside"])),
		(0, 3, lambda: GameObject(Adjective("burlap", Noun("sack")), spaces=["inside"])),
		(0, 3, lambda: GameObject(Adjective("wooden", Noun("crate")), spaces=["inside"])),
		
		(0, 4, lambda: GameObject(Adjective("oak", Noun("barrel")), spaces=["inside"])),
		(2, 4, lambda: GameObject(Adjective("dusty", Noun("shelf")), spaces=["on"])),
		(2, 4, lambda: GameObject(Adjective("storage", Noun("chest")), spaces=["on"])),
		(2, 4, lambda: GameObject(Adjective("storage", Noun("cabinet")), spaces=["inside"])),
		
		(3, 10, lambda: GameObject(Noun("end table"), spaces=["on"])),
		(3, 10, lambda: GameObject(Adjective("mahogany", Noun("table")), spaces=["on"])),
		(4, 10, lambda: GameObject(Adjective("writing", Noun("desk")), spaces=["on", "inside"])),
		(2, 4, lambda: GameObject(Adjective("fine", Adjective("wooden", Noun("shelf"))), spaces=["on"])),
		(4, 8, lambda: GameObject(Preposition(Noun("chest"), "of drawers"), spaces=["on", "inside"])),
		
		(8, 10, lambda: GameObject(Adjective("ornate", Adjective("display", Noun("case"))), spaces=["inside"])),
		(8, 10, lambda: GameObject(Adjective("gilded", Adjective("sea", Noun("chest"))), spaces=["on", "in"]))
]

#######################
# Room titles
#
# These tuples include the minimum/maximum opulence the room title should be used for
#######################
roomTitles = [
		# Very opulent rooms
		(8, 10, "Decorated Hallway"),
		(9, 10, "Master Bedroom"),
		(8, 10, "Grand Ballroom"),
		(8, 10, "Private Study"),
		(8, 10, "Fine Washroom"),
		
		# Opulent rooms
		(6, 8, "Guest Bedroom"),
		(6, 8, "Study"),
		(5, 8, "Drawing Room"),
		(5, 8, "Dining Room"),
		
		# Functional rooms
		(4, 6, "Water closet"),
		(4, 6, "Conservatory"),
		(3, 6, "Halway"),
		(3, 4, "Pantry"),
		
		# Dismal rooms
		(2, 4, "Servants' Quarters"),
		(2, 4, "Kitchen"),
		(1, 3, "Narrow Corridor"),
		(0, 1, "Dank Cell")
]

#######################
# Room decor
#
# These tuples include the minimum/maximum opulence the room decor element applies to
#######################
roomDecor = [
		(0, 1, "The unintelligible writings of some hasty hand plaster the walls."),
		(0, 1, "A cool sweat of moisture covers the stone walls."),
		(0, 1, "Bits of straw scrape softly underfoot."),
		(0, 1, "Rodents make their nests in the gaps in the unattended masonry."),
		(1, 3, "Sturdy timbers support the ceiling's weight."),
		(3, 5, "Rodents make their nests in the gaps in the unattended masonry."),
		(5, 7, "A Persian rug rests on the exotic hardwood floor."),
		(5, 10, "Rich mahogany panels run from floor to ceiling."),
		(7, 8, "A silver candelabra hangs from the celing."),
		(7, 10, "Paintings of Biblical saints seem to glow faintly."),
		(9, 10, "The walls are crowned by exquisitely carved moulding."),
		(9, 10, "A priceless crystal chandelier hangs from the ceiling.")
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
	
# Generates a Location given a MazeCell
# The room's "opulence" is derived from its distance from the starting room,
# and factors generating the room's features
def makeLocation(mazeCell):
	opulence = min(10, mazeCell.distance)
	
	# Room title
	validTitles = [title for (min, max, title) in roomTitles if min <= opulence <= max]
	title = random.choice(validTitles)
	
	# Descriptive elements
	numDecor = random.randint(1, 3)
	validDecor = [decor for (min, max, decor) in roomDecor if min <= opulence <= max]
	decors = [random.choice(validDecor) for i in range(numDecor)]
	description = " ".join(list(set(decors)))
	
	location = Location(title, description, opulence)
		
	# Objects in room
	numObjects = random.randint(1, 4)
	for i in range(numObjects):
		object = makeObject(location)
		location.objects.append(object)
		
	return location
	
def makeItem(location):
	validItemGenerators = [gen for (min, max, gen) in itemGenerators if min <= location.opulence <= max]
	makeItem = random.choice(validItemGenerators)
	return makeItem()
	
def makeObject(location):
	generators = [gen for (min, max, gen) in objectGenerators if min <= location.opulence <= max]
	
	makeObject = random.choice(generators)
	object = makeObject()
	
	# Add items
	for space in object.getSpaces():		
		numItems = random.randint(1, 4)
		for i in range(numItems):			
			item = makeItem(location)
			object.getSpace(space).add(item)
	
	return object
	
def connect(locationA, locationB, direction, inverse):
	locationA.addDoor(direction, locationB)
	locationB.addDoor(inverse, locationA)