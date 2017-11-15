import unittest
from Array.rev_word import rev_word as sol


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sol('    space before'), 'before space')
        self.assertEqual(sol('space after     '), 'after space')
        self.assertEqual(sol('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(sol('1'), '1')


if __name__ == '__main__':
    unittest.main()
