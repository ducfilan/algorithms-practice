class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head):
    prev_node = head.next_node
    i_node = prev_node.next_node
    prev_prev_node = head
    prev_prev_node.next_node = None

    while i_node.next_node is not None:
        prev_node.next_node = prev_prev_node
        prev_prev_node = prev_node
        prev_node = i_node
        i_node = i_node.next_node
    else:
        prev_node.next_node = prev_prev_node

    i_node.next_node = prev_node