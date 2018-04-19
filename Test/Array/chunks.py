import unittest
from Array.chunks import chunk


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(chunk([1, 2, 3, 4], 2), [[ 1, 2], [3, 4]])
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[ 1, 2], [3, 4], [5]])
        self.assertEqual(chunk([1, 2, 3, 4, 5, 6, 7, 8], 3), [[ 1, 2, 3], [4, 5, 6], [7, 8]])
        self.assertEqual(chunk([1, 2, 3, 4, 5], 4), [[ 1, 2, 3, 4], [5]])
        self.assertEqual(chunk([1, 2, 3, 4, 5], 10), [[ 1, 2, 3, 4, 5]])


if __name__ == '__main__':
    unittest.main()
