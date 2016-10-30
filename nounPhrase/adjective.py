
from nounPhrase.indefinite import Indefinite
from nounPhrase.definite import Definite

class Adjective(object):
	def __init__(self, adjective, nounPhrase):
		self.adjective = adjective
		self.nounPhrase = nounPhrase
		
	def stripAdjectives(self):
		return self.nounPhrase.stripAdjectives()
		
	def pluralize(self):
		return Adjective(self.adjective, self.nounPhrase.pluralize())
		
	def makeIndefinite(self):
		return Indefinite(self)
		
	def makeDefinite(self):
		return Definite(self)
		
	def toString(self, formatNonArticles=None):
		string = self.adjective + " " + self.nounPhrase.toString()
		if formatNonArticles:
			string = formatNonArticles(string)
		return string
		
	def isIdentifiedBy(self, string):
		return string in [self.toString(), self.stripAdjectives().toString()]