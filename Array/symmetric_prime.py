from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def find_next_prime(prime):
    found = False

    while not found:
        prime = prime + 1

        if is_prime(prime):
            found = True

    return prime if found else -1


def find_prev_prime(prime):
    found = False

    while not found and prime > 1:
        prime = prime - 1

        if is_prime(prime):
            found = True

    return prime if found else -1


def symmetric_prime(a, b):
    prev_prime = -1
    curr_prime = -1

    first_prime = -1
    last_prime = -1

    res = 0

    for i in range(a, b + 1):
        if i == 1:
            continue

        if is_prime(i):
            last_prime = i
            if prev_prime == -1:
                prev_prime = i
                first_prime = i
                continue

            if curr_prime == -1:
                curr_prime = i
                continue

            next_prime = i

            if next_prime != -1 and curr_prime == (prev_prime + next_prime) / 2:
                res += 1

            prev_prime = curr_prime
            curr_prime = next_prime

    if res == 0:
        curr_prime = first_prime
        next_prime = find_next_prime(curr_prime)
        prev_prime = find_prev_prime(curr_prime)

        res += 1 if next_prime > 0 and prev_prime > 0 and next_prime != -1 and curr_prime == (
                prev_prime + next_prime) / 2 else 0

        curr_prime = last_prime
        next_prime = find_next_prime(curr_prime)
        prev_prime = find_prev_prime(curr_prime)

        res += 1 if next_prime > 0 and prev_prime > 0 and next_prime != -1 and curr_prime == (
                prev_prime + next_prime) / 2 else 0

    return res


print(symmetric_prime(1, 4))
