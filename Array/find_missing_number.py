def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # find the first number missing from its index, that will be our required number
    for i in range(n):
        if nums[i] != i:
            return i

    return n


def find_missing_number2(nums):
    for i, num in enumerate(nums):
        correct_pos = num
        nums[correct_pos], nums[i] = nums[i], nums[correct_pos]

    return nums[-1]


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    print(find_missing_number2([3, 1, 2, 0, 2, 4]))


main()
