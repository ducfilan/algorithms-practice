# Find all ways to sum to n using integers from 1 to n.

result = []
sum_to_index = [0]


def sum_to_n(n, j=1):
    for i in range(1, n - sum_to_index[j - 1] + 1):
        sum_to_index.append(0)
        sum_to_index[j] = sum_to_index[j - 1] + i

        if sum_to_index[j] > n:
            break
        elif sum_to_index[j] == n:
            result.append(i)
            print(result)
            del result[-(len(result) - j + 2):]
            break
        else:
            result.append(i)
            sum_to_n(n, j + 1)


if __name__ == '__main__':
    sum_to_n(6)
