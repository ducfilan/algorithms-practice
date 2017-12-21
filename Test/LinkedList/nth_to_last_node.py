import unittest
from LinkedList.nth_to_last_node import nth_to_last_node as sol, nth_to_last_node2 as sol2, Node


class MyTestCase(unittest.TestCase):
    def test_solution1(self):
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
        self.assertEqual(sol(6,a), None)

    def test_solution2(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)

        a.next_node = b
        b.next_node = c
        c.next_node = d
        d.next_node = e

        self.assertEqual(sol2(2,a), 4)
        self.assertEqual(sol2(4,a), 2)
        self.assertEqual(sol2(5,a), 1)
        self.assertEqual(sol2(6,a), None)


if __name__ == '__main__':
    unittest.main()
