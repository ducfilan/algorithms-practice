def fib_rec(n, memo=None):
    if not memo:
        memo = [1, 1]
        memo += [0] * (n - 2)

    if memo[n - 1]:
        return memo[n - 1]

    return fib_rec(n - 1, memo) + fib_rec(n - 2, memo)
