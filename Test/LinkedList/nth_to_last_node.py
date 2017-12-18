import unittest
from LinkedList.nth_to_last_node import nth_to_last_node as sol, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)

        a.next_node = b
        b.next_node = c
        c.next_node = d
        d.next_node = e

        self.assertEqual(sol(2,a), 4)
        self.assertEqual(sol(4,a), 2)
        self.assertEqual(sol(5,a), 1)
        self.assertEqual(sol(6,a), -1)


if __name__ == '__main__':
    unittest.main()
