import unittest
from StacknQueue.balance_check import balance_check as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol('[](){([[[]]])}('), False)
        self.assertEqual(sol('[{{{(())}}}]((()))'), True)
        self.assertEqual(sol('[[[]])]'), False)
        self.assertEqual(sol('()(){]}'), False)
        self.assertEqual(sol('()'), True)
        self.assertEqual(sol('('), False)
        self.assertEqual(sol(''), True)


if __name__ == '__main__':
    unittest.main()
