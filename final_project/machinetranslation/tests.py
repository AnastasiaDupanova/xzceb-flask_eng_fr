import unittest
from translator import english_to_french
from translator import french_to_english
class test_english_to_french (unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test2(self): 
        self.assertNotEqual(english_to_french(0), 0)

class test_french_to_english (unittest.TestCase): 
    def test3(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test4(self): 
        self.assertNotEqual(french_to_english(0), 0)

unittest.main()
