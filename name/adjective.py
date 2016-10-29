
class Adjective(object):
	def __init__(self, value, clause):
		self.value = value
		self.clause = clause
		
	def simplify(self):
		return self.clause.simplify()
		
	def toString(self):
		return self.value + " " + self.clause.toString()