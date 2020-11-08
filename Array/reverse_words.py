# Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words).
# Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).

def revert_list(l):
    list_end_pos = len(l) - 1
    mid_pos = list_end_pos // 2
    for i in range(mid_pos + 1):
        # swap
        l[i], l[list_end_pos - i] = l[list_end_pos - i], l[i]

def reverse_words(words):
    if not words:
        return words

    word_start = 0

    for word_end in range(len(words)):
        if word_end == (len(words) - 1) or words[word_end + 1] == ' ':
            middle_pos = (word_end - word_start) // 2
            for i in range(middle_pos + 1):
                # swap
                words[word_start + i], words[word_end - i] = words[word_end - i], words[word_start + i]

            word_start = word_end + 2

    revert_list(words)

s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can

s = list("")
reverse_words(s)
print(''.join(s))

s = list("duc filan ")
reverse_words(s)
print(''.join(s))

s = list("test  test  ")
reverse_words(s)
print(''.join(s))
