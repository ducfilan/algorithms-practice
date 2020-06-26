# This problem was asked by Lyft.
#
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.


def contiguous_sum_to_k(list, k):
    sum = 0
    elements = []

    for num in list:
        if sum < k:
            sum += num
            elements.append(num)
        elif sum > k:
            sum -= elements[0]
            del elements[0]

        if sum == k:
            return elements

    return None


print(contiguous_sum_to_k([1, 2, 3, 4, 5], 9))
