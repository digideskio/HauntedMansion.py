
import nounPhrase as nounPhraseModule
from nounPhrase.indefinite import Indefinite
from nounPhrase.definite import Definite

class Preposition(object):
	def __init__(self, nounPhrase, preposition, hasVowelSound=None):
		self.nounPhrase = nounPhrase
		self.preposition = preposition
		
		if hasVowelSound is not None:
			self.hasVowelSound = hasVowelSound
		else:
			self.hasVowelSound = nounPhrase.hasVowelSound
		
	def stripAdjectives(self):
		return self.nounPhrase.stripAdjectives()
		
	def pluralize(self):
		return Preposition(self.nounPhrase.pluralize(), self.preposition)
		
	def makeIndefinite(self):
		return Indefinite(self)
		
	def makeDefinite(self):
		return Definite(self)
		
	def toString(self, formatNonArticles=None):
		string = self.nounPhrase.toString() + " " + self.preposition
		if formatNonArticles:
			string = formatNonArticles(string)
		return string
		
	def isIdentifiedBy(self, string):
		return string in [self.toString(), self.stripAdjectives().toString()]