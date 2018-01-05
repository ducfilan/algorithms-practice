import unittest
from Array.max_adjacent_distance import solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(solution([-1, 3, -4, 5, 1, -6, 2, 1]), 7)
        self.assertEqual(solution([0, 3, 3, 7, 5, 3, 11 ,1]), 7)
        self.assertEqual(solution([1]), -1)
        self.assertEqual(solution([1, 1]), -1)


if __name__ == '__main__':
    unittest.main()
