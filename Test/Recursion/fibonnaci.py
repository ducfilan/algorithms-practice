import unittest
from Recursion.fibonnaci import fib_rec as solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(solution(10), 55)
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(23), 28657)


if __name__ == '__main__':
    unittest.main()
