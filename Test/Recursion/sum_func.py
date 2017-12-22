import unittest
from Recursion.sum_func import sum_func


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sum_func(4321), 4+3+2+1)


if __name__ == '__main__':
    unittest.main()
