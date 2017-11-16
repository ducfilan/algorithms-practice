# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
# For this problem, you can falsely "compress" strings of single or double letters.
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
#
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


def compress(s):
    if s == '':
        return ''

    output = ''
    count = 1
    curr_char = s[0]

    for c in s[1:]:
        if curr_char == c:
            count += 1
        else:
            output += curr_char + str(count)
            count = 1
            curr_char = c

    output += curr_char + str(count)

    return output
