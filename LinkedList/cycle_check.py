# Given a singly linked list, write a function which takes in the first node in a singly linked list
# and returns a boolean indicating if the linked list contains a "cycle".
#
# A cycle is when a node's next point actually points back to a previous node in the list.
# This is also sometimes known as a circularly linked list.


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check(node):
    visited_nodes = { node }
    i_node = node

    while i_node.next_node is not None:
        if i_node.next_node in visited_nodes:
            return True

        visited_nodes.add(i_node.next_node)
        i_node = i_node.next_node

    return False
