import unittest
from Array.birthday_cake_candles import birthday_cake_candles


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(birthday_cake_candles(4, [3, 2, 1, 3]), 2)


if __name__ == '__main__':
    unittest.main()
