'''
Find the maximum value in a given Bitonic array. 
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array, arr[i] != arr[i+1].

Example: Input: [1, 3, 8, 12, 4, 2], Output: 12
'''

def bitonic_array_maximum(arr):
    if not arr or len(arr) == 0:
        return None

    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start)//2

        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return arr[start]

print(bitonic_array_maximum([]))
print(bitonic_array_maximum([1]))
print(bitonic_array_maximum([1, 2, 3]))
print(bitonic_array_maximum([1, -1, -2, 1, 3, 5]))
print(bitonic_array_maximum([1, 3, 8, 12, 4, 2]))