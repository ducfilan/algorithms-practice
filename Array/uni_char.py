# Given a string, determine if it is comprised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return false.


def uni_char(s):
    chars = set()

    for c in s:
        if c not in chars:
            chars.add(c)
        else:
            return False

    return True
