# Create a function called word_split() which takes in a string phrase and a set list_of_words.
# The function will then determine if it is possible to split the string in a way in which
# words can be made from the list of words. You can assume the phrase will only contain words
# found in the dictionary if it is completely splittable.


def word_split(phrase, list_of_words):
    for word in list_of_words:
        if phrase.startswith(word):
            list_of_words.remove(word)
            return [word] if word == phrase else [word] + word_split(phrase[len(word):], list_of_words)

    return []
