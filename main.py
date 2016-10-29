from game import Game

def main():	
	game = Game()
	print("Welome to the game.")
	print()
	
	game.look()
	
	while(True):
		print()
		command = input(">")
		execute(command, game)
	
def execute(command, game):
	words = command.split(" ")
	if not words:
		return
		
	first = words[0]
	rest = " ".join(words[1:])

	if (first == "look"):		
		game.look()
	elif (first in ["go", "move"]):
		game.movePlayer(words[1])
	elif (first == "inventory"):
		game.inventory()
	elif (first == "get"):
		# TODO validate rest
		game.get(rest)
	else:
		print("Command not recognized");

	
main()