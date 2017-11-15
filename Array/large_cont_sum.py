# Given an array of integers (positive and negative) find the largest continuous sum.
#
# So the input:
#
# large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
#
# would return:
#
#  29


def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    sum_val = max_val = arr[0]

    for i in arr[1:]:
        sum_val += i

        if sum_val < i:
            sum_val = i

        if sum_val > max_val:
            max_val = sum_val

    return max_val
