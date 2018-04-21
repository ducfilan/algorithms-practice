# Write a function that takes a head node and an integer value n
# and then returns the nth to last node in the linked list.


from LinkedList.node import Node


def nth_to_last_node(n, head):
    trace_arr = []
    i = head

    while i.next_node:
        trace_arr.append(i.value)
        i = i.next_node
        if len(trace_arr) > n:
            trace_arr = trace_arr[1:]

    if len(trace_arr) < n - 1:
        return None

    if len(trace_arr) == n - 1:
        return trace_arr[0]

    return trace_arr[1]


def nth_to_last_node2(n, head):
    left, right = head, head

    for i in range(n-1):
        if not right.next_node:
            return None

        right = right.next_node

    while right.next_node:
        left = left.next_node
        right = right.next_node

    return left.value
