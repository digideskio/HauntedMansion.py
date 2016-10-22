
import name

class IndefiniteName(object):
	def __init__(self, name):
		self.name = name
		
	def getDeclarative(self):
		return ("an " if name.startsWithVowel(self.name) else "a ") + self.name