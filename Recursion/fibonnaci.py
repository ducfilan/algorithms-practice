def fib_rec(n, memo=None):
    if not memo:
        memo = [1, 1]
        memo += [0] * (n - 2)

    if memo[n - 1]:
        return memo[n - 1]

    return fib_rec(n - 1, memo) + fib_rec(n - 2, memo)


def fib_bottom_up(n):
    fib_numbers = [0, 1, 1]
    fib_numbers += [0] * (n - 2)

    for i in range(3, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers[n]