import unittest
from Recursion.coin_change import coin_change as solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        coins = [1, 5, 10, 25]
        self.assertEqual(solution(45, coins), 3)
        self.assertEqual(solution(23, coins), 5)
        self.assertEqual(solution(74, coins), 8)


if __name__ == '__main__':
    unittest.main()
