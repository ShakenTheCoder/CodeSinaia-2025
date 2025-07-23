import unittest
from TODO_number_to_words import number_to_words


class TestUnits(unittest.TestCase):
    
    def test_zero(self):
        self.assertEqual(number_to_words(0), "zero")
    def test_one(self):
        self.assertEqual(number_to_words(1), "one")
class TestTens(unittest.TestCase):
    
    def test_twenty(self):
        self.assertEqual(number_to_words(20), "twenty")
    def test_thirty(self):
        self.assertEqual(number_to_words(30), "thirty")
    def test_forty(self):
        self.assertEqual(number_to_words(40), "forty")
    def test_fifty(self):
        self.assertEqual(number_to_words(50), "fifty")
    def test_sixty(self):
        self.assertEqual(number_to_words(60), "sixty")
    def test_seventy(self):
        self.assertEqual(number_to_words(70), "seventy")
    def test_eighty(self):
        self.assertEqual(number_to_words(80), "eighty")
    def test_ninety(self):
        self.assertEqual(number_to_words(90), "ninety")