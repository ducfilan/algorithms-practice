def min_heapify(arr, i):
    left = i * 2 + 1
    right = left + 1

    min_index = i

    nodes_count = len(arr)

    if left < nodes_count and arr[left] < arr[min_index]:
        min_index = left

    if right < nodes_count and arr[right] < arr[min_index]:
        min_index = right

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        min_heapify(arr, min_index)


def build_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr, i)

    return arr

print(build_min_heap([1, 9, 8, 2, 3, 10, 14, 7, 16, 4]))
