# Given the mapping a = 1, b = 2, … z = 26, and an encoded message count the number of ways it can be decoded.
# For example, the message ‘111’ would give 3, since it could be decoded as ‘aaa’, ‘ka’, and ‘ak’.
# You can assume that the messages are decodable and that the given data string has only digits between 0 and 9.
# For example, ‘001’ is not allowed.


alphabet = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def num_ways(data, memo={}):
    if len(data) == 0 or data[0] == '0':
        return None

    if len(data) == 1:
        return [alphabet[int(data)]]

    if len(data) == 2:
        output = [] if '0' in data else [alphabet[int(data[0])] + alphabet[int(data[1])]]
        data_int = int(data)
        if data_int <= 26:
            output += alphabet[data_int]

        return output

    if data in memo:
        return memo[data]

    result = list(dict.fromkeys([(way1 + way2) for way1 in num_ways(data[:1]) for way2 in num_ways(data[1:])] +
                                [(way1 + way2) for way1 in num_ways(data[:2]) for way2 in num_ways(data[2:])]))

    memo[data] = result

    return result


def num_ways_count(data, memo={}):
    if data.startswith('0'):
        return 0

    if len(data) <= 1:
        return 1

    if len(data) in memo:
        return memo[len(data)]

    result = num_ways_count(data[1:], memo)

    if int(data[:2]) <= 26:
        result += num_ways_count(data[2:], memo)

    memo[len(data)] = result

    return result


print(num_ways('123123123'))
print(num_ways_count('123123123'))
print(num_ways('01'))
print(num_ways('10'))
