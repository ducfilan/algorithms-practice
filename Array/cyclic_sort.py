def cyclic_sort(array):
    for i in range(len(array)):
        while array[i] != i + 1:
            correct_position = array[i] - 1
            array[i], array[correct_position] = array[correct_position], array[i]

    return array


print(cyclic_sort([3, 1, 2, 7, 6, 4, 5]))
