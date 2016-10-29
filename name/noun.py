
class Noun(object):
	def __init__(self, value):
		self.value = value
		
	def simplify(self):
		return self
		
	def toString(self):
		return self.value