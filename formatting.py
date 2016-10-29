
from colorama import Fore, Back, Style

def oxfordComma(items):
	if(len(items) == 1):
		return str(items[0])
	if(len(items) == 2):
		return items[0] + " and " + items[1]
	return ", ".join(
			items[0:len(items)-1]
	) + ", and " + items[len(items)-1]
	
def title(string):
	return Style.BRIGHT + Fore.GREEN + string + Style.RESET_ALL
	
def door(string):
	return Fore.GREEN + string + Style.RESET_ALL
	
def itemNames(items):
	return [itemName(item.name.getDeclarative()) for item in items]
	
def itemName(string):
	return Fore.YELLOW + string + Style.RESET_ALL
	