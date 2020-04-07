# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def connect(self, next_node):
        self.next = next_node


class Solution:
    def __init__(self, nodes_value):
        prev_node = Node(nodes_value[0])
        self.first_node = prev_node

        for value in nodes_value[1:]:
            next_node = Node(value)
            prev_node.connect(next_node)
            prev_node = next_node

    def detect(self):
        slow_pointer = self.first_node
        fast_pointer = self.first_node.next

        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

            if fast_pointer == slow_pointer:
                return True

        return False


s = Solution([1, 2, 3, 4, 5, 6, 7])

s.first_node.next.next.next.next.next.next.next = s.first_node.next.next

print(s.detect())
