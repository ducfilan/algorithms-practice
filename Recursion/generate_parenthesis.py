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


generate_parenthesis(3)
