import unittest
from Array.finder import finder


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(finder([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)

if __name__ == '__main__':
    unittest.main()
