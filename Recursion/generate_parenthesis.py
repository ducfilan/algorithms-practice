# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def generate_parenthesis(N):
    ans = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * N:
            ans.append(s)
            return
        if left < N:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return ans


print(generate_parenthesis(3))
