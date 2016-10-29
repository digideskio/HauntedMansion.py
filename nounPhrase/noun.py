
from nounPhrase.indefinite import Indefinite
from nounPhrase.definite import Definite

class Noun(object):
	def __init__(self, value):
		self.value = value
		
	def stripAdjectives(self):
		return self
		
	def makeIndefinite(self):
		return Indefinite(self)
		
	def makeDefinite(self):
		return Definite(self)
		
	def toString(self):
		return self.value
		
	def isIdentifiedBy(self, string):
		return string == self.value