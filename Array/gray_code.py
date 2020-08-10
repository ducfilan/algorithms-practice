# Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around.
# Gray code is common in hardware so that we don't see temporary spurious values during transitions.
#
# Given a number of bits n, generate a possible gray code for it.
#
# For example, for n = 2, one gray code would be [00, 01, 11, 10].

def gray_code(n):
    start = ['0'] * n
    res = [''.join(start)]

    for i in range(n - 1, -1, -1):
        if start[i] == '0':
            start[i] = '1'
            res.append(''.join(start))

    for i in range(n - 1, 0, -1):
        if start[i] == '1':
            start[i] = '0'
            res.append(''.join(start))

    return res


print(gray_code(2))
print(gray_code(3))
