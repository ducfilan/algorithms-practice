# Given an unsorted array of numbers, find Kth smallest number in it.
# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

from heapq import heappush, heappop


def find_Kth_smallest_number(nums, k):
    top_k_smallest = []

    for num in nums[:k]:
        heappush(top_k_smallest, -num)

    for num in nums[k:]:
        if top_k_smallest[0] < -num:
            heappop(top_k_smallest)
            heappush(top_k_smallest, -num)

    return -top_k_smallest[0]


print(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
