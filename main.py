from game import Game

def main():	
	game = Game()
	print("Welome to the game.")
	print()
	
	game.look()
	
	while(True):
		command = input(">")
		execute(command, game)
	
def execute(command, game):
	words = command.split(" ")
	if not words:
		return

	if (words[0] == "look"):		
		game.look()
	elif (words[0] == "go" or words[0] == "move"):
		game.movePlayer(words[1])
	elif (words[0] == "inventory"):
		game.inventory()
	else:
		print("Command not recognized");

	
main()