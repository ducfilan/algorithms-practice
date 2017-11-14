# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
#
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
#
# Input:
#
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
#
# Output:
#
# 5 is the missing number


def count_appear(arr):
    appear_arr = {}

    for i in arr:
        if i in appear_arr:
            appear_arr[i] += 1
        else:
            appear_arr[i] = 1

    return appear_arr


def finder(arr1, arr2):
    appear_arr1 = count_appear(arr1)
    appear_arr2 = count_appear(arr2)

    for k,v in appear_arr1.items():
        if k not in appear_arr2 or v != appear_arr2[k]:
            return k