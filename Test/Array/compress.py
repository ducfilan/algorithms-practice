import unittest
from Array.compress import compress as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol(''), '')
        self.assertEqual(sol('AABBCC'), 'A2B2C2')
        self.assertEqual(sol('AAABCCDDDDD'), 'A3B1C2D5')
        self.assertEqual(sol('AAAABBBBCCCCCDDEEEE'), 'A4B4C5D2E4')
        self.assertEqual(sol('AAB'), 'A2B1')
        self.assertEqual(sol('A'), 'A1')


if __name__ == '__main__':
    unittest.main()
