import unittest
from Recursion.coin_change import coin_change, coin_change_dynamic


class MyTestCase(unittest.TestCase):
    def test_recursive_memoize(self):
        coins = [1, 5, 10, 25]
        self.assertEqual(coin_change(45, coins), 3)
        self.assertEqual(coin_change(23, coins), 5)
        self.assertEqual(coin_change(74, coins), 8)

    def test_dynamic(self):
        coins = [1, 5, 10, 25]
        self.assertEqual(coin_change_dynamic(45, coins), 3)
        self.assertEqual(coin_change_dynamic(23, coins), 5)
        self.assertEqual(coin_change_dynamic(74, coins), 8)


if __name__ == '__main__':
    unittest.main()
