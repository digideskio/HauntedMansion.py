
import name

class IndefiniteName(object):
	def __init__(self, clause):
		self.clause = clause
		
	def getDefinite(self):
		clauseString = self.clause.toString()
		return "the " + clauseString
		
	def getDeclarative(self):
		clauseString = self.clause.toString()
		return ("an " if name.startsWithVowel(clauseString) else "a ") + clauseString
		
	def simplify(self):
		return IndefiniteName(self.clause.simplify())
		
	def identifiedBy(self, name):
		return name in [self.clause.toString(), self.clause.simplify().toString()]