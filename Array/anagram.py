def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for c in s1:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in s2:
        if c in count:
            count[c] -= 1
        else:
            return False

    for c in count:
        if count[c] != 0:
            return False

    return True
