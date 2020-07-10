from itertools import groupby
from operator import itemgetter


def mostCommonWords(text, n):
    words = text.split()
    words_dict = {word.lower(): 0 for word in words}

    for word in words:
        words_dict[word.lower()] += 1
    words_dict = {
        k: sorted(list(map(itemgetter(0), v)))
        for k, v in groupby(sorted(words_dict.items(), key=itemgetter(1), reverse=True), itemgetter(1))
    }

    result = [word for group_words in list(words_dict.values()) for word in group_words][:n]
    return result + [""] * (n - len(result))


print(mostCommonWords("He is a pupil", 1))
print(mostCommonWords("He is a pupil", 1) == ["a"])
print(mostCommonWords("He is a pupil", 5))
print(mostCommonWords("He is a pupil", 5) == ["a", "he", "is", "pupil", ""])
print(mostCommonWords("He is a pupil, and she is a student", 2))
print(mostCommonWords("He is a pupil, and she is a student", 2) == ["a", "is"])
print(mostCommonWords("He is a pupil, and she is a student ", 3))
print(mostCommonWords("He is a pupil, and she is a student ", 3) == ["a", "is", "and"])
