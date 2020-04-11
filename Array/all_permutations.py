def gen_all_permutations(arr):
    if len(arr) <= 1:
        return [arr]

    permutations = []

    for i in range(len(arr)):
        permutations += [[arr[i]] +
                         sub_permutations for sub_permutations in gen_all_permutations(arr[:i] + arr[i+1:])]

    return permutations


print(gen_all_permutations([1, 2, 3]))
