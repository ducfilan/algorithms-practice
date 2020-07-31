# To get a software development project done, FJP engineers need to create a special algorithm which adds a bracket
# pair ("()") such that the return value of the given expression is the largest possible one.
#
# Given a string expression including numbers 1 to 9 and two operators '+' and '*', which represents an expression.
# Write a function that returns the largest possible result when adding a bracket pair to the given expression.
#
# Example:
#
# For expression = "3+5*2+6*4", the output should be maximum_result(expression) = 163
# Explanation: We can add a bracket pair as follows: "3+5*(2+6)*4"
# The result of the new expression is 163.
# For expression = "5+5*5+5*5", the output should be maximum_result(expression) = 255
# Explanation: We can add a bracket pair as follows: "5+5*(5+5)*5"
# The result of the new expression is 255.


import re


def maximum_result(expression):
    regex1 = '(((\d+)\*)+\d*)\**(\d+)'
    matches = re.finditer(regex1, expression, re.MULTILINE)

    muls = [
        (match.start(0) + len(re.split(r'[\+\*]', match.group(0))[0]), match.start(4))
        for match in matches
    ]

    if len(muls) == 0:
        return eval(expression)

    if len(muls) == 1:
        matches = re.finditer(regex1, expression, re.MULTILINE)
        match = [match for match in matches][0]
        start, end = match.start(0), match.end(0)

        match_parts = re.split(r'[\+\*]', match.group(0))

        start += len(match_parts[0])
        end -= len(match_parts[-1])

        return max(eval('(' + expression[:start] + ')' + expression[start:]),
                   eval(expression[:end] + '(' + expression[end:] + ')'))

    max_val = -1

    for i in range(len(muls) - 1):
        for j in range(i + 1, len(muls)):
            start = muls[i][1]
            end = muls[j][0]

            max_val = max(max_val, eval(expression[:start] + '(' + expression[start:end] + ')' + expression[end:]))

    return max_val


print(maximum_result('2+7+8*8*7+1+3+6*5*3*7*3*2+8+5*1+5*5+9*6+6*5+1*3+8+5'))
