import unittest
from LinkedList.reverse import reverse as sol, Node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Create a list of 4 nodes
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)

        # Set up order a,b,c,d with values 1,2,3,4
        a.next_node = b
        b.next_node = c
        c.next_node = d

        sol(a)

        self.assertEqual(d.next_node, c)
        self.assertEqual(c.next_node, b)
        self.assertEqual(b.next_node, a)
        self.assertEqual(a.next_node, None)

        a = Node('a')
        sol(a)

        a = Node('a')
        b = Node('b')

        a.next_node = b

        sol(a)

        self.assertEqual(b.next_node, a)
        self.assertEqual(a.next_node, None)


if __name__ == '__main__':
    unittest.main()
