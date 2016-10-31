
import nounPhrase as nounPhraseModule
from nounPhrase.indefinite import Indefinite
from nounPhrase.definite import Definite

class Noun(object):
	def __init__(self, value, irregularPlural=None):
		self.value = value
		self.irregularPlural = irregularPlural
		
	def pluralize(self):
		if self.irregularPlural is not None:
			return Noun(self.irregularPlural)
	
		lastLetter = self.value[-1]
		if lastLetter == "y" and not nounPhraseModule.isVowel(self.value[-2]):
			pluralForm = self.value[0:-1] + "ies"
		elif lastLetter in ["s", "x"]:
			pluralForm = self.value + "es"
		else:
			pluralForm = self.value + "s"
		return Noun(pluralForm)
		
	def stripAdjectives(self):
		return self
		
	def makeIndefinite(self):
		return Indefinite(self)
		
	def makeDefinite(self):
		return Definite(self)
		
	def toString(self, formatNonArticles=None):
		return formatNonArticles(self.value) if formatNonArticles else self.value
		
	def isIdentifiedBy(self, string):
		return string == self.value