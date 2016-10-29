
import nounPhrase as nounPhraseModule

class Definite(object):
	def __init__(self, nounPhrase):
		self.nounPhrase = nounPhrase
		
	def toString(self):
		return "the " + self.nounPhrase.toString()
	
	def makeDefinite(self):
		return self
		
	def makeIndefinite(self):
		return nounPhraseModule.Indefinite(self.nounPhrase)
		
	def stripAdjectives(self):
		return Definite(self.nounPhrase.stripAdjectives())
		
	def isIdentifiedBy(self, name):
		return name in [self.nounPhrase.toString(), self.nounPhrase.stripAdjectives().toString()]