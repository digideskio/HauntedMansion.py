
import nounPhrase as nounPhraseModule
from nounPhrase.indefinite import Indefinite
from nounPhrase.definite import Definite

class Noun(object):
	def __init__(self, value):
		self.value = value
		
	def pluralize(self):
		# TODO also allow an irregular plural form to be passed
		if self.value[-1] == "y" and not nounPhraseModule.isVowel(self.value[-2]):
			pluralForm = self.value[0:-1] + "ies"
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