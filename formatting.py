
from colorama import Fore, Back, Style

def oxfordComma(items, conjunction="and"):
	if len(items) == 1:
		return str(items[0])
	if len(items) == 2 :
		return items[0] + " " + conjunction + " " + items[1]
		
	return ", ".join(
			items[0:len(items)-1]
	) + ", " + conjunction + " " + items[len(items)-1]
	
def number(n):
	# TODO generalize this
	return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][n]
	
def title(string):
	return Style.BRIGHT + Fore.GREEN + string + Style.RESET_ALL
	
def door(string):
	return Fore.GREEN + string + Style.RESET_ALL
	
def inventoryItems(inventory):
	strings = []

	for key in inventory.itemsByName:
		items = inventory.itemsByName[key]
		item = items[0]
		if len(items) == 1:
			strings.append(itemName(item, item.name.makeIndefinite()))
		else:
			strings.append(number(len(items)) + " " + itemName(item, item.name.pluralize()))
		
	return strings
	
def itemNamesIndefinite(items):
	return [itemName(item, item.name.makeIndefinite()) for item in items]
	
def itemNamesDefinite(items):
	return [itemName(item, item.name.makeDefinite()) for item in items]
	
def itemName(item, name=None):
	if not name:
		name = item.name
		
	textColor = Fore.RED if item.isWeapon else Fore.YELLOW
	format = lambda text: textColor + text + Style.RESET_ALL
		
	return name.toString(format)
	