# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"


def max_char(s):
    if not s:
        return None

    char_dict = {}

    for c in s:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    char_max = None
    char_max_count = 0

    for c, count in char_dict.items():
        if count > char_max_count:
            char_max_count = count
            char_max = c

    return char_max
