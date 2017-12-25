import unittest
from Recursion.permute import permute as solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sorted(solution('abc')), sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(sorted(solution('dog')), sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))
        self.assertEqual(solution(''), [''])
        self.assertEqual(solution('a'), ['a'])
        self.assertEqual(solution('aaa'), ['aaa', 'aaa','aaa', 'aaa','aaa', 'aaa'])


if __name__ == '__main__':
    unittest.main()
