
from nounPhrase.definite import Definite

class AlwaysDefinite(Definite):
	def makeIndefinite(self):
		return self