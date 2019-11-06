# How do you find all permutations of a string?


def permutations(s):
    if len(s) == 2:
        return [s, s[1] + s[0]]

    all_sub_permutations = permutations(s[1:])
    return [s[0] + x for x in all_sub_permutations] + [x + s[0] for x in all_sub_permutations]


print(permutations('internet'))
