# Given a singly linked list, write a function which takes in the first node in a singly linked list
# and returns a boolean indicating if the linked list contains a "cycle".
#
# A cycle is when a node's next point actually points back to a previous node in the list.
# This is also sometimes known as a circularly linked list.


from LinkedList.node import Node


def cycle_check(node):
    visited_nodes = { node }
    i_node = node

    while i_node.next_node is not None:
        if i_node.next_node in visited_nodes:
            return True

        visited_nodes.add(i_node.next_node)
        i_node = i_node.next_node

    return False


def cycle_check_2(node):
    follow_node = node
    lead_node = node.next_node

    while lead_node is not None:
        if lead_node == follow_node:
            return True

        lead_node = lead_node.next_node.next_node
        follow_node = follow_node.next_node

    return False
