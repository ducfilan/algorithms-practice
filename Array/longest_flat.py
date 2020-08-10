# Write a function which takes a list of numbers and returns the length of the longest continuous stretch
# of a single number. For example, on the input [1,7,7,3], the correct return is 2, because there are two 7's in a row.

def longest_flat(array):
    if not array:
        return 0

    array += [array[-1] + 1]

    max_res = 0
    start = 0
    end = 0
    for end in range(len(array)):
        if array[start] != array[end]:
            max_res = max(max_res, end - start)
            start = end

    max_res = max(max_res, end - start)

    return max_res


print(longest_flat([1, 1, 1]))
print(longest_flat([1, 1, 1, -2, -2, -2, -2, 3, 3, 3]))
