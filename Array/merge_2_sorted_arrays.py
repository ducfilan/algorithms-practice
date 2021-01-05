def merge_2_sorted_arrays(a1, a2):
    i1, i2 = 0, 0
    l1, l2 = len(a1), len(a2)

    merged_a  = []

    while i1 < l1 and i2 < l2:
        if a1[i1] < a2[i2]:
            merged_a.append(a1[i1])
            i1 += 1
        else:
            merged_a.append(a2[i2])
            i2 += 1

    while i1 < l1:
        merged_a.append(a1[i1])
        i1 += 1
    
    while i2 < l2:
        merged_a.append(a2[i2])
        i2 += 1

    return merged_a

print(merge_2_sorted_arrays([], []))
print(merge_2_sorted_arrays([], [1, 2, 3]))
print(merge_2_sorted_arrays([1, 4, 7], []))
print(merge_2_sorted_arrays([1, 4, 7], [2, 5, 6]))
print(merge_2_sorted_arrays([1, 4, 7, 8, 9], [2, 5, 6]))
print(merge_2_sorted_arrays([1, 4, 7, 10, 111, 333], [22, 52, 62, 122]))
