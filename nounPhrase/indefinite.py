
import nounPhrase as nounPhraseModule

class Indefinite(object):
	def __init__(self, nounPhrase):
		self.nounPhrase = nounPhrase
		
	def toString(self, formatNonArticles=None):
		phraseString = self.nounPhrase.toString()
		startsWithVowel = nounPhraseModule.startsWithVowel(phraseString)
		if (formatNonArticles):
			phraseString = formatNonArticles(phraseString)
		return ("an " if startsWithVowel else "a ") + phraseString
		
	def pluralize(self):
		return Indefinite(self.nounPhrase.pluralize())
	
	def makeDefinite(self):
		return nounPhraseModule.Definite(self.nounPhrase)
		
	def makeIndefinite(self):
		return self
		
	def stripAdjectives(self):
		return Indefinite(self.nounPhrase.stripAdjectives())
		
	def isIdentifiedBy(self, name):
		return name in [self.nounPhrase.toString(), self.nounPhrase.stripAdjectives().toString()]