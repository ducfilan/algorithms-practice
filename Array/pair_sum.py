# Given an integer array, output all the unique pairs that sum up to a specific value k.
#
# So the input:
#
# pair_sum([1,3,2,2],4)
#
# would return 2 pairs:
#
#  (1,3)
#  (2,2)
#
# NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS


def pair_sum(arr, k):
    count = 0
    trace = set()

    for e in arr:
        if e in trace:
            count += 1
        else:
            trace.add(k - e)

    return count


def is_pair_sum_exists(nums, target):
    start, end = 0, len(nums) - 1

    while start < end:
        sum = nums[start] + nums[end]
        if sum > target:
            end -= 1
        elif sum < target:
            start += 1

        return True

    return False


print(is_pair_sum_exists([1, 2, 3, 4, 6], 6))
