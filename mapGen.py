from location import Location
import random
import mazeGen
from item import Item
from nounPhrase.adjective import Adjective
from nounPhrase.noun import Noun

itemGenerators = [
	lambda: Item(Adjective("exquisite", Noun("candlestick"))),
	lambda: Item(Adjective("wooden", Noun("candlestick"))),
	lambda: Item(Noun("key")),
	lambda: Item(Adjective("silver", Noun("dagger")), isWeapon=True),
	lambda: Item(Adjective("herbal", Noun("remedy")))
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
	level = min(10, mazeCell.distance)
	validTitles = [title for (title, min, max) in roomTitles if min <= level <= max]
	title = random.choice(validTitles)
	
	description = random.choice(roomDecor)
	description += " " + random.choice(roomDecor)
	
	location = Location(title, description, mazeCell.distance)
	
	if random.random() > 0.0:
		numItems = random.randint(1, 3)
		for i in range(numItems):
			item = random.choice(itemGenerators)()
			location.inventory.add(item)
	
	return location
	
def connect(locationA, locationB, direction, inverse):
	locationA.addDoor(direction, locationB)
	locationB.addDoor(inverse, locationA)