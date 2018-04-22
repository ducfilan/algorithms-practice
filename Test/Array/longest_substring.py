import unittest
from Array.longest_substring import longest_substring


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(longest_substring('pwwkew'), 3)
        self.assertEqual(longest_substring('dvdf'), 3)


if __name__ == '__main__':
    unittest.main()
