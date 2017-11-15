import unittest
from Array.large_cont_sum import large_cont_sum as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(sol([-1, 1]), 1)
        self.assertEqual(sol([-5, -1, -2, -4, -3]), -1)
        self.assertEqual(sol([]), 0)


if __name__ == '__main__':
    unittest.main()
