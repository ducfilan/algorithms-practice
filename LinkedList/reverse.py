# Write a function to reverse a Linked List in place.
# The function will take in the head of the list as input and return the new head of the list.


from LinkedList.node import Node


def reverse(head):
    current_node = head
    previous_node = None

    while current_node:
        next_node = current_node.next_node
        current_node.next_node = previous_node
        previous_node = current_node
        current_node = next_node

    return current_node
