from location import Location
import random
import mazeGen
from item import Item
from name.indefiniteName import IndefiniteName
from name.adjective import Adjective
from name.noun import Noun

roomTemplates = [
		("Cavernous Hall", "Flying buttresses support the lofty ceiling."),
		("Dank Cell", "The ceiling sits oppressively low."),
		("Corridor", "The stones in the wall sit at an uncomfortable angle."),
]

roomDecor = [
	"Ancient bas-reliefs depict scenes of treachery and descruction.",
	"The unintelligible writings of some hasty hand plaster the walls.",
	"Once-fine wood carvings have long turned to dust."
]

def createMaze(width, height):
	(maze, startingCell) = mazeGen.randomizedPrim(width, height)
	
	# initialize the locations
	rooms = []
	for row in range(0, height):
		roomsRow = []
		rooms.append(roomsRow)
		for col in range(0, width):
			location = makeLocation()
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
	
def makeItem():
	val = random.random()
	if val > 0.75:
		return Item(IndefiniteName(Adjective("exquisite", Noun("candlestick"))))
	elif val > 0.50:
		return Item(IndefiniteName(Adjective("wooden", Noun("candlestick"))))
	elif val > 0.25:
		return Item(IndefiniteName(Adjective("unburnt", Noun("torch"))))
	else:
		return Item(IndefiniteName(Adjective("silver", Noun("dagger"))))
	
def makeLocation():
	(name, description) = random.choice(roomTemplates)
	description += " " + random.choice(roomDecor)
	
	location = Location(name, description)
	
	if random.random() > 0.0:
		numItems = random.randint(1, 3)
		for i in range(numItems):
			item = makeItem()
			location.inventory.add(item)
	
	return location
	
def connect(locationA, locationB, direction, inverse):
	locationA.addDoor(direction, locationB)
	locationB.addDoor(inverse, locationA)