import unittest
from Array.max_char import max_char


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(max_char('abcccccccd'), 'c')
        self.assertEqual(max_char(''), None)
        self.assertEqual(max_char(None), None)


if __name__ == '__main__':
    unittest.main()
