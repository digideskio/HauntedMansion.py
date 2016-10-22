def oxfordComma(items):
	if(len(items) == 1):
		return str(items[0])
	if(len(items) == 2):
		return items[0] + " and " + items[1]
	return ", ".join(
			items[0:len(items)-1]
	) + ", and " + items[len(items)-1]