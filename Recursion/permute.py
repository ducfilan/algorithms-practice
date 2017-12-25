# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.
# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Note: If a character is repeated, treat each occurence as distinct, for example an input of 'xxx'
#       would return a list with 6 "versions" of 'xxx'


def permute(s):
    output = []
    if len(s) <= 1:
        return [s]

    for i, letter in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            output += [letter + perm]

    return output
