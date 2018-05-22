def three_sum(a):
    if not a or len(a) < 3:
        return []

    a_dict = {k: v for k, v in enumerate(a)}

    a.sort()
    result = []
    start, end = 0, len(a) - 1
    start_i, end_i = start, end

    if a[start] > 0 or a[end] < 0:
        return []

    if a[start] == a[end]:
        if a[start] == 0:
            return [[0, 0, 0]]
        else:
            return []

    while a[start_i] < 0:
        triple = None
        couple_result = a[start] + a[end_i]
        target_value = 0 - couple_result

        if target_value in a_dict:
            triple = [a[start], target_value, a[end_i]]

        if target_value < 0 and target_value < a[start]:
            start += 1
            end_i = end

        elif target_value > 0 and target_value > a[end_i]:
            end -= 1
            start_i = start

        if triple:
            result.append(triple)

    clean_result = []
    for i in result:
        if i not in clean_result:
            clean_result.append(i)

    return clean_result


print(three_sum([1, -1]) == [])
print(three_sum([0, 0, 0]) == [[0, 0, 0]])
print(three_sum([1, 2, -2, -1]) == [])
print(three_sum([-4, -2, -1]) == [])
print(three_sum([1, -1, -1, 0]) == [[-1, 0, 1]])
print(three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]])
print(three_sum([3, 0, -2, -1, 1, 2]) == [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]])
print(three_sum([1, 1, -2]) == [[-2, 1, 1]])
print(three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
print(three_sum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]])
print(three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]],
      three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))