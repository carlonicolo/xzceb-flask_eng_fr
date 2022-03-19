import unittest

from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(""), "")
        self.assertEqual(englishToFrench(""), "")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

        