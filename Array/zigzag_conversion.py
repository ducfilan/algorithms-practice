# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
# Example 1:
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


def zigzag_conversion(s, num_rows):
    n = len(s)

    if n <= num_rows or num_rows == 1:
        return s

    output = ''
    steps = 2 * (num_rows - 1)
    base_steps = []

    for i in range(0, n + steps - 1, steps):
        if i < n:
            output += s[i]
        base_steps.append(i)

    visited_set = set()
	
    escalator = 1
    while len(output) < n:
        for i in base_steps:
            pre_i = i - escalator
            pos_i = i + escalator

            if pre_i > 0 and pre_i < n and pre_i not in visited_set:
                output += s[pre_i]
                visited_set.add(pre_i)

            if pos_i < n and pos_i not in visited_set:
                output += s[pos_i]
                visited_set.add(pos_i)

        escalator += 1

    return output
