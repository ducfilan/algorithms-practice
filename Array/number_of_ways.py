# The sequence t0, t1, t2, ..., tn is called a ZIG-ZAG sequence if t0 < t1 > t2 < t3 > t4, etc.
# Given an integer sequence arr, write a function that returns the number of pairs (i, j) where i < j such that after
# swapping arr[i]and arr[j], arr becomes a ZIG-ZAG sequence. If there is no way to swap 2 numbers in order to
# convert arr into a ZIG-ZAG sequence, return 0.
# The input data is guaranteed that the arr sequence is not a ZIG-ZAG sequence.
# Example:
# For arr = [2, 9, 3, 8, 8], the output should be numberOfWays(arr) = 2.
# Explanation: there are 2 pairs (i, j):
# i = 0, j = 4, after swapping arr[i] and arr[j], we have arr = [8, 9, 3, 8, 2].
# i = 1, j = 3, after swapping arr[i] and arr[j], we have arr = [2, 8, 3, 9, 8].
# For arr = [4, 3, 2, 6, 2], the output should be numberOfWays(arr) = 3.
# Explanation: there are 3 pairs (i, j):
#
#
# i = 0, j = 1, after swapping arr[i] and arr[j], we have arr = [3, 4, 2, 6, 2].
# i = 0, j = 4, after swapping arr[i] và arr[j], we have arr = [2, 3, 2, 6, 4].
# i = 1, j = 3, after swapping arr[i] và arr[j], we have arr = [4, 6, 2, 3, 2].
# For arr = [1, 2, 3, 4, 5, 6, 7], the output should be numberOfWays(arr) = 0.
# Explanation: there is no pair(i, j) such that arr becomes a ZIG-ZAG sequence.

a = []
n = 0


def numberOfWays(arr):
    global a, n
    a = arr
    n = len(a)

    wrong_position_places = []

    if n == 2:
        return 1 if a[0] > a[1] else 0

    for i in range(n):
        if i % 2 == 0:
            if (i > 0 and a[i - 1] <= a[i]) or (i < n - 1 and a[i] >= a[i + 1]):
                wrong_position_places.append(i)
        else:
            if (i > 0 and a[i - 1] >= a[i]) or (i < n - 1 and a[i] <= a[i + 1]):
                wrong_position_places.append(i)

    if len(wrong_position_places) > 6:
        return 0

    res = 0
    cache = set()

    for i in wrong_position_places:
        for j in range(0, n):
            swap_pair = (min(i, j), max(i, j))
            if swap_pair in cache:
                continue

            cache.add(swap_pair)

            a[i], a[j] = a[j], a[i]

            if i != j and is_correct_position(i) and is_correct_position(j):
                is_zigzag = True
                for ii in wrong_position_places:
                    if not is_correct_position(ii):
                        is_zigzag = False
                        break
                if is_zigzag:
                    res += 1

            a[i], a[j] = a[j], a[i]

    return res


def is_correct_position(i):
    if i < 0 or i > n - 1:
        return True

    if i % 2 == 0:
        if (i == 0 or a[i - 1] > a[i]) and (i == n - 1 or a[i] < a[i + 1]):
            return True
    else:
        if (i == 0 or a[i - 1] < a[i]) and (i == n - 1 or a[i] > a[i + 1]):
            return True

    return False


print(numberOfWays([4, 2, 2, 4, 4]))  # 1
print(numberOfWays([2, 1]))  # 1
print(numberOfWays([1, 2, 3, 4, 5, 6, 7]))  # 0
print(numberOfWays([2, 4, 1, 7, 6, 9, 10, 9, 6, 9, 6]))  # 2
print(numberOfWays([4, 3, 2, 6, 2]))  # 3
print(numberOfWays([2, 9, 3, 8, 8]))  # 2
print(numberOfWays([4, 3, 2, 6, 2]))  # 3
print(numberOfWays([1, 27, 12, 26, 24, 27, 11, 4, 1, 22, 3, 12, 2, 1, 5, 20, 5, 15, 3, 13]))  # 1
