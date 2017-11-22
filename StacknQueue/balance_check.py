# Given a string of opening and closing parentheses, check whether it’s balanced.
# We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}.
# Assume that the string doesn’t contain any other character than these, no spaces words or numbers.
# As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened.
# For example ‘([])’ is balanced but ‘([)]’ is not.
#
# You can assume the input string has no spaces.


def balance_check(s):
    if s == '':
        return True

    if len(s) % 2 != 0:
        return False

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    open_brackets = ['(', '{', '[']
    balance_list = []

    for c in s:
        if c in open_brackets:
            balance_list.append(brackets[c])
        else:
            if balance_list.pop() != c:
                return False

    if balance_list:
        return False

    return True
