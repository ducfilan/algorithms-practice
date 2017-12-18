# Write a function that takes a head node and an integer value n
# and then returns the nth to last node in the linked list.


class Node(object):
    def __init__(self, value):
        self.next_node = None
        self.value = value


def nth_to_last_node(n, head):
    trace_arr = []
    i = head

    while i.next_node:
        trace_arr.append(i.value)
        i = i.next_node
        if len(trace_arr) > n:
            trace_arr = trace_arr[1:]

    return -1 if len(trace_arr) < n - 1 else trace_arr[0 if len(trace_arr) == n - 1 else 1]
