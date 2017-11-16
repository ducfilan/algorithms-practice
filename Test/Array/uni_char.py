import unittest
from Array.uni_char import uni_char as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol(''), True)
        self.assertEqual(sol('goo'), False)
        self.assertEqual(sol('abcdefg'), True)


if __name__ == '__main__':
    unittest.main()
