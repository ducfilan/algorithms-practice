import unittest
from Array.compress import compress as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol(''), '')
        self.assertEqual(sol('AABBCC'), 'A2B2C2')
        self.assertEqual(sol('AAABCCDDDDD'), 'A3B1C2D5')


if __name__ == '__main__':
    unittest.main()
