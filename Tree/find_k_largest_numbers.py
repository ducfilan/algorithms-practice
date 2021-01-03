# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

from heapq import heappop, heappush


def find_k_largest_numbers(nums, k):
    if k >= len(nums):
        return nums

    top_k_largest = []

    for num in nums[:k + 1]:
        heappush(top_k_largest, num)

    for num in nums[k + 1:]:
        heappop(top_k_largest)
        heappush(top_k_largest, num)

    heappop(top_k_largest)

    return top_k_largest

print(find_k_largest_numbers([], 1))
print(find_k_largest_numbers([1], 2))
print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
print(find_k_largest_numbers([11, 12, 5, 3, 1, 2], 3))
