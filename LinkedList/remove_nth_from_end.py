# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# 
# Given n will always be valid.


def remove_nth_from_end(head, n):
    if n == 1 and not head.next_node:
        return None

    node_count = 1
    start_node, end_node = head, head

    while end_node.next_node:
        if node_count <= n:
            node_count += 1

        if node_count == n + 1:
            start_node = start_node.next_node
        end_node = end_node.next_node

    if node_count < n - 1:
        return head

    if start_node == head:
        return start_node.next_node

    start_node.next = start_node.next.next_node

    return head
