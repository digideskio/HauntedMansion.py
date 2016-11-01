from game import Game
import colorama

def main():	
	colorama.init()
	print("Welome to the game.")
	
	print()
	game = Game()
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
		game.movePlayer(rest)
	elif (first == "inventory"):
		game.inventory()
	elif (first == "get"):
		# TODO validate rest
		game.get(rest)
	else:
		print("Command not recognized");

	
main()