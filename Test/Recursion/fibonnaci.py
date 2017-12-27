import unittest
from Recursion.fibonnaci import fib_rec as solution, fib_bottom_up


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(solution(10), 55)
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(23), 28657)

    def test_fib_bottom_up(self):
        self.assertEqual(fib_bottom_up(10), 55)
        self.assertEqual(fib_bottom_up(1), 1)
        self.assertEqual(fib_bottom_up(23), 28657)


if __name__ == '__main__':
    unittest.main()
