# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

from heapq import heappush, heappop


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __lt__(self, other):
        return self.value < other.value


class SortedListsMerger:
    def __init__(self, lists):
        self.lists = [self._to_linked_list(l) for l in lists]

    def _to_linked_list(self, l):
        if not l:
            return None

        l.append(None)

        root = current_node = Node(l[0])
        for i in range(1, len(l) - 1):
            current_node.next = Node(l[i])
            current_node = current_node.next

        return root

    def merge_lists(self):
        merged_list = []

        min_heap = []

        for root in self.lists:
            if root:
                heappush(min_heap, root)

        while min_heap:
            min_heap_root = heappop(min_heap)

            merged_list.append(min_heap_root.value)
            if min_heap_root.next:
                heappush(min_heap, min_heap_root.next)

        return merged_list


merger = SortedListsMerger([[2, 6, 8], [3, 6, 7], [1, 3, 4]])
print(merger.merge_lists())
