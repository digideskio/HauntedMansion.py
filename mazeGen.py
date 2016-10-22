import random

class Link(object):
	def __init__(self, direction, source, dest):
		self.direction = direction
		self.source = source
		self.dest = dest
		
class Cell(object):
	def __init__(self, position, visited, doors, walls):
		self.position = position
		self.visited = visited
		self.doors = doors
		self.walls = walls

def getCell(grid, pos):
	(row, col) = pos
	return grid[row][col]
	
def opposite(direction):
	if direction == "North":
		return "South"
	if direction == "South":
		return "North"
	if direction == "East":
		return "West"
	if direction == "West":
		return "East"
	
def connectCells(wall, source, dest):
	for sourceWall in source.walls:
		if sourceWall.direction == wall.direction:
			# Change the wall to a door
			source.walls.remove(sourceWall)
			source.doors.append(sourceWall)
	
	reverseDir = opposite(wall.direction)
	for destWall in dest.walls:
		if destWall.direction == reverseDir:
			# Change the wall to a door
			dest.walls.remove(destWall)
			dest.doors.append(destWall)	
				
# Creates a map using a randomized Prim's algorithm
# The map is a minimum spanning tree of the grid, that is, it contains no cycles.
def randomizedPrim(mapWidth, mapHeight):
	# Initalize the grid
	grid = []
	for row in range(0, mapHeight):
		gridRow = []
		grid.append(gridRow)
		for col in range(0, mapWidth):
			cell = Cell((row, col), False, [], [])
			if row > 0:
				cell.walls.append(Link("South", (row, col), (row-1, col)))
			if row < mapHeight-1:
				cell.walls.append(Link("North", (row, col), (row+1, col)))
			if col > 0:
				cell.walls.append(Link("West", (row, col), (row, col-1)))
			if col < mapHeight-1:
				cell.walls.append(Link("East", (row, col), (row, col+1)))
			
			gridRow.append(cell)
			
	walls = []
	startingCell = grid[mapHeight-1][0] # TODO pick a random outside cell	
	startingCell.visited = True
	walls.extend(startingCell.walls)
	
	while (walls.__len__() > 0):
		# pick a random wall
		wall = random.choice(walls)
		cellA = getCell(grid, wall.source)
		cellB = getCell(grid, wall.dest)
		
		if cellA.visited and not cellB.visited:
			connectCells(wall, cellA, cellB)
			cellB.visited = True
			walls.extend(cellB.walls)
		if cellB.visited and not cellA.visited:
			connectCells(wall, cellA, cellB)
			cellA.visited = True
			walls.extend(cellA.walls)
		walls.remove(wall)
			
	return (grid, startingCell)