# Given a set with distinct elements, find all of its distinct subsets.


def gen_subsets(nums):
    subsets = [[]]

    if not nums:
        return subsets

    for num in nums:
        n = len(subsets)

        for i in range(n):
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)

    return subsets


print(gen_subsets([1, 3, 5]))
