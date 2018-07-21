# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


def divide(dividend, divisor):
    sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

    dividend = abs(dividend)
    divisor = abs(divisor)

    sum = divisor
    quotient = 0

    while sum <= dividend:
        sum += divisor
        quotient += 1

    return quotient if sign else -quotient
