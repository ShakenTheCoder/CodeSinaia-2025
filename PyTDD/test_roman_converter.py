import unittest
from roman_converter import roman_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)
    # ======== Step 2 ======== 
    def test_no_str(self):
        self.assertEqual(roman_converter("a"), None)
    def test_num_vir(self):
        self.assertEqual(roman_converter(3.9), None)

    def test_range_min(self):
        self.assertEqual(roman_converter(0), None)
    def test_range_max(self):
        self.assertEqual(roman_converter(4001), None)

class TestOnes(unittest.TestCase):
    def test_base_1(self):
        self.assertEqual(roman_converter(1), "I")
    def test_base_2(self):
        self.assertEqual(roman_converter(2), "II")
    def test_base_3(self):
        self.assertEqual(roman_converter(3), "III")
    

class TestFives(unittest.TestCase):
    def test_base_5(self):
        self.assertEqual(roman_converter(5), "V")
class TestTens(unittest.TestCase):    
    def test_base_10(self):
        self.assertEqual(roman_converter(10), "X")
    def test_base_25(self):
        self.assertEqual(roman_converter(25), "XXV")
    def test_base_50(self):
        self.assertEqual(roman_converter(50), "L")

