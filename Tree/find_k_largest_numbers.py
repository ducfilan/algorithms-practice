# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

from heapq import heappop, heappush


def find_k_largest_numbers(nums, k):
    top_k_largest = []

    for num in nums[:k]:
        heappush(top_k_largest, num)

    for num in nums[k:]:
        heappop(top_k_largest)
        heappush(top_k_largest, num)

    return top_k_largest


print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
