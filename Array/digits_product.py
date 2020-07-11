# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of
# whose digits is equal to product. If there is no such integer, return -1 instead.
#
# Example
#
# For product = 12, the output should be digitsProduct(product) = 26;
# For product = 19, the output should be digitsProduct(product) = -1.

import itertools


def factors(n):
    f = 2
    increments = itertools.chain([1, 2, 2], itertools.cycle([4, 2, 4, 2, 4, 6, 2, 6]))
    for incr in increments:
        if f * f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n


def digitsProduct(product):
    if product == 0:
        return 10

    if product < 10:
        return product

    prime_factors = list(factors(product))
    if prime_factors[-1] > 10:
        return -1

    if len(prime_factors) == 1:
        return -1

    i = 0
    while i < len(prime_factors) and prime_factors[i] < 5:
        i += 1

    after_5 = prime_factors[i:]
    before_5 = prime_factors[:i]

    before_5_zip = []

    while len(before_5) >= 2:
        digit_result = before_5[-1] * before_5[-2]
        before_5.pop()
        before_5.pop()
        if digit_result == 4 and len(before_5) >= 1:
            digit_result *= before_5[-1]
            before_5.pop()
        before_5_zip.append(digit_result)

    return int(''.join(str(i) for i in sorted(before_5 + before_5_zip + after_5)))
