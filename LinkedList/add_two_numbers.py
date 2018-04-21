# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


from LinkedList.node import Node


def add_two_numbers(l1, l2):
    result_nodes = []
    remember_val = 0

    current_node_l1, current_node_l2 = l1, l2

    while True:
        result_val = (current_node_l1.value if current_node_l1 else 0) + (current_node_l2.value if current_node_l2 else 0) + remember_val

        if result_val > 9:
            result_val -= 10
            remember_val = 1
        else:
            remember_val = 0

        result_nodes.append(Node(result_val))

        current_node_l1, current_node_l2 = current_node_l1.next_node if current_node_l1 else None, current_node_l2.next_node if current_node_l2 else None
        if not current_node_l1 and not current_node_l2:
            break

    if remember_val:
        result_nodes.append(Node(remember_val))

    for i in range(len(result_nodes) - 1):
        result_nodes[i].next_node = result_nodes[i+1]

    return result_nodes[0]
