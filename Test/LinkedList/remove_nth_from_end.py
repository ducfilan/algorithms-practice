import unittest
from LinkedList.node import Node
from LinkedList.remove_nth_from_end import remove_nth_from_end

class MyTestCase(unittest.TestCase):
    def test_something(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)

        node1.next_node = node2
        # node2.next_node = node3
        # node3.next_node = node4
        # node4.next_node = node5

        remove_nth_from_end(node1, 2)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
