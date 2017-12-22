# Given an integer, create a function which returns the sum of all the individual digits in that integer.
# For example: if n = 4321, return 4+3+2+1


def sum_func(n):
    return n if n < 10 else n % 10 + sum_func(int(n/10))
