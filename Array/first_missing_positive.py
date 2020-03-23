# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.


def first_missing_positive(nums):
    if nums is None:
        return 1

    nums_set = set(nums)

    missing_positive = 1

    while missing_positive in nums_set:
        missing_positive += 1

    return missing_positive


print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))
print(first_missing_positive(None))
print(first_missing_positive([]))
