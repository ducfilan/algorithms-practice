class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head):
    current_node = head
    previous_node = None
    next_node = Node

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node

    return current_node
