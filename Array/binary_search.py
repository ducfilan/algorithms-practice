def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle
        if middle < target:
            start = middle + 1
        else:
            end = middle - 1

    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
