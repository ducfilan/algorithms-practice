import unittest
from Recursion.factorial import factorial as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol(4), 24)


if __name__ == '__main__':
    unittest.main()
