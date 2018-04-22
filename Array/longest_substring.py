# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a sub-sequence and not a substring.


def longest_substring(s):
    char_dict = {}
    longest_count = 0

    for i, c in enumerate(s):
        if c in char_dict:
            longest_count = max(longest_count, len(char_dict))
            dup_i = char_dict[c]
            char_dict = {k: v for k, v in char_dict.items() if v > dup_i}

        char_dict[c] = i

    return max(longest_count, len(char_dict))
