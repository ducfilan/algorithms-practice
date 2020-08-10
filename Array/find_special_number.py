from math import pow, log, floor


def find_special_number(n, k):
    max_pow = int(floor(log(n, k)))
    res = pow(k, max_pow)
    max_res = pow(k, max_pow + 1)

    for i in range(max_pow):
        res += pow(k, i)
        if res >= max_res:
            break
        if res >= n:
            return int(res) % 1000000007

    return int(max_res) % 1000000007


print(find_special_number(8, 3))  # 9
print(find_special_number(10, 3))  # 10
print(find_special_number(92, 13))  # 169
print(find_special_number(100, 3))  # 108
print(find_special_number(2003, 131))  # 17161
print(find_special_number(5356, 42))  # 74088
