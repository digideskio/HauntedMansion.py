
import nounPhrase as nounPhraseModule

class Indefinite(object):
	def __init__(self, nounPhrase):
		self.nounPhrase = nounPhrase
		
	def toString(self):
		phraseString = self.nounPhrase.toString()
		return ("an " if nounPhraseModule.startsWithVowel(phraseString) else "a ") + phraseString
	
	def makeDefinite(self):
		return nounPhraseModule.Definite(self.nounPhrase)
		
	def makeIndefinite(self):
		return self
		
	def stripAdjectives(self):
		return Indefinite(self.nounPhrase.stripAdjectives())
		
	def isIdentifiedBy(self, name):
		return name in [self.nounPhrase.toString(), self.nounPhrase.stripAdjectives().toString()]