import unittest
from Recursion.word_split import word_split


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(word_split('themanran',['the','ran','man']), ['the', 'man', 'ran'])
        self.assertEqual(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']), ['i', 'love', 'dogs', 'John'])
        self.assertEqual(word_split('themanran',['clown','ran','man']), [])


if __name__ == '__main__':
    unittest.main()
