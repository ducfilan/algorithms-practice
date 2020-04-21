# Given a string, find all of its permutations preserving the character sequence but changing case.
#
# Example 1:
#
# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"
# Example 2:
#
# Input: "ab7c"
# Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"


def find_letter_case_string_permutations(s):
    if not s or len(s) == 0:
        return s

    if len(s) == 1:
        if s.isalpha():
            return [s, s.upper()]
        else:
            return [s]

    permutations = []

    sub_perms = find_letter_case_string_permutations(s[1:])
    permutations += [s[0] + perm for perm in sub_perms]
    if s[0].isalpha():
        permutations += [s[0].swapcase() + perm for perm in sub_perms]

    return permutations


print(find_letter_case_string_permutations('ad52'))
print(find_letter_case_string_permutations('ab7c'))
