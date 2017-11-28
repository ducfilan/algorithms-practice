import unittest
from LinkedList.cycle_check import cycle_check as sol, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # CREATE CYCLE LIST
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)

        a.next_node = b
        b.next_node = c
        c.next_node = d
        d.next_node = b  # Cycle Here!

        # CREATE NON CYCLE LIST
        x = Node(1)
        y = Node(2)
        z = Node(3)

        x.next_node = y
        y.next_node = z

        self.assertEqual(sol(a), True)
        self.assertEqual(sol(x), False)


if __name__ == '__main__':
    unittest.main()
