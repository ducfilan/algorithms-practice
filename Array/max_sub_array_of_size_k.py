# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
#
# Example 1:
#
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:
#
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].


def max_sub_array_of_size_k(k, arr):
    if k == 0 or len(arr) < k:
        return 0

    max_sub_array_sum = 0

    start = 0
    max_sub_array_sum = 0
    sub_array_elements = []

    for end, num in enumerate(arr):
        sub_array_elements.append(num)

        if len(sub_array_elements) >= k:
            sub_array_sum = sum(sub_array_elements)
            max_sub_array_sum = max(max_sub_array_sum, sub_array_sum)

            sub_array_elements.pop(0)

    return max_sub_array_sum


print('pass' if max_sub_array_of_size_k(
    3, [2, 1, 5, 1, 3, 2]) == 9 else 'fail')
print('pass' if max_sub_array_of_size_k(
    0, [2, 1, 5, 1, 3, 2]) == 0 else 'fail')
print('pass' if max_sub_array_of_size_k(3, []) == 0 else 'fail')
print('pass' if max_sub_array_of_size_k(3, [1]) == 0 else 'fail')
