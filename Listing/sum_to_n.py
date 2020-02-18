result = []
sum_to_index = [0]
j = [1]


def sum_to_n(n):
    for i in range(1, n - sum_to_index[j[0] - 1] + 1):
        sum_to_index.append(sum_to_index[j[0] - 1] + i)

        if sum_to_index[j[0]] > n:
            break
        elif sum_to_index[j[0]] == n:
            result.append(i)
            print(result)
            result.pop()
            break
        else:
            j[0] = j[0]+1
            result.append(i)
            sum_to_n(n)


if __name__ == '__main__':
    sum_to_n(6)
