import unittest
from Recursion.reverse_string import reverse_string


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('hello world'), 'dlrow olleh')
        self.assertEqual(reverse_string('123456789'), '987654321')


if __name__ == '__main__':
    unittest.main()
