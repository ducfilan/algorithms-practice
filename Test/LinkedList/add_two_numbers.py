import unittest
from LinkedList.node import Node
from LinkedList.add_two_numbers import add_two_numbers


class MyTestCase(unittest.TestCase):
    def test_something(self):
        l1_node1 = Node(2)
        l1_node2 = Node(4)
        l1_node3 = Node(3)

        l1_node1.next_node = l1_node2
        l1_node2.next_node = l1_node3

        l2_node1 = Node(5)
        l2_node2 = Node(6)
        l2_node3 = Node(4)

        l2_node1.next_node = l2_node2
        l2_node2.next_node = l2_node3

        l3_node1 = Node(7)
        l3_node2 = Node(0)
        l3_node3 = Node(8)

        l3_node1.next_node = l3_node2
        l3_node2.next_node = l3_node3

        result = add_two_numbers(l1_node1, l2_node1)

        self.assertEqual(result.value, l3_node1.value)
        self.assertEqual(result.next_node.value, l3_node2.value)
        self.assertEqual(result.next_node.next_node.value, l3_node3.value)


if __name__ == '__main__':
    unittest.main()
