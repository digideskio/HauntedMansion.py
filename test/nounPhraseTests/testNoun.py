import unittest

from test.nounPhraseTests import testFormat
from nounPhrase.noun import Noun

class NounTest(unittest.TestCase):
	
	def test_toString(self):
		noun = Noun("test")
		self.assertEqual("test", noun.toString())

	def test_toString_format(self):
		noun = Noun("test")
		string = noun.toString(testFormat)
		self.assertEqual("[test]", string)

	def test_vowelSound_vowel(self):
		noun = Noun("artichoke")
		self.assertEqual(True, noun.hasVowelSound)
		
	def test_vowelSound_consonant(self):
		noun = Noun("pepperoni")
		self.assertEqual(False, noun.hasVowelSound)
		
	def test_vowelSound_irregularTrue(self):
		noun = Noun("herb", hasVowelSound=True)
		self.assertEqual(True, noun.hasVowelSound)
		
	def test_vowelSound_irregularFalse(self):
		noun = Noun("user", hasVowelSound=False)
		self.assertEqual(False, noun.hasVowelSound)
		
	def test_pluralize_vowel(self):
		noun = Noun("pizza")
		self.assertEqual("pizzas", noun.pluralize().toString())
		
	def test_pluralize_consonant(self):
		noun = Noun("crust")
		self.assertEqual("crusts", noun.pluralize().toString())
		
	def test_pluralize_ay(self):
		noun = Noun("bay")
		self.assertEqual("bays", noun.pluralize().toString())
		
	def test_pluralize_y(self):
		noun = Noun("pasty")
		self.assertEqual("pasties", noun.pluralize().toString())
		
	def test_pluralize_s(self):
		noun = Noun("boss")
		self.assertEqual("bosses", noun.pluralize().toString())
		
	def test_pluralize_x(self):
		noun = Noun("box")
		self.assertEqual("boxes", noun.pluralize().toString())
		
	def test_pluralize_irregular(self):
		noun = Noun("mouse", irregularPlural="mice")
		self.assertEqual("mice", noun.pluralize().toString())
		
if __name__ == '__main__':
    unittest.main()