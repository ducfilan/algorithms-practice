# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.


def missing_number(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            correct_position = nums[i] - 1
            if nums[i] == nums[correct_position]:
                return nums[i]

            nums[i], nums[correct_position] = nums[correct_position], nums[i]
    return -1


print(missing_number([4, 3, 1, 3]))
