import unittest
from Others.divide_intergers import divide


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(divide(10, 3), 3)
        self.assertEqual(divide(7, -3), -2)
        self.assertEqual(divide(1, 1), 1)


if __name__ == '__main__':
    unittest.main()
