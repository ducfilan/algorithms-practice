# Level: EASY
#
# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
#
# Example 1:
#
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:
#
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:
#
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].


def smallest_subarray_with_given_sum(array, s):
    array = array or []
    smallest_subarray = []

    smallest_length = len(array)
    sum = 0

    for num in array:
        sum += num
        smallest_subarray.append(num)

        while sum >= s:
            smallest_length = min(smallest_length, len(smallest_subarray))
            sum -= smallest_subarray.pop(0)

    return smallest_length


print('passs' if smallest_subarray_with_given_sum(
    [2, 1, 5, 2, 3, 2], 7) == 2 else 'fail')
print('passs' if smallest_subarray_with_given_sum(
    [2, 1, 5, 2, 8], 7) == 1 else 'fail')
print('passs' if smallest_subarray_with_given_sum(
    [3, 4, 1, 1, 6], 8) == 3 else 'fail')
