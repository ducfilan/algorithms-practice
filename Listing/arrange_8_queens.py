result = []


def arrange_8_queens(queen_no=1):
    for i in range(1, 9):
        is_next = False
        for r in result:
            if i in r or r[0] + r[1] == i + queen_no or r[0] - r[1] == i - queen_no:
                is_next = True
                continue
        if is_next:
            if i == 8:
                del result[:]

            continue

        if len(result) <= queen_no:
            result.append((i, queen_no))
        else:
            result[queen_no] = (i, queen_no)

        if len(result) == 8:
            print(result)
        elif queen_no < 8:
            arrange_8_queens(queen_no + 1)


if __name__ == '__main__':
    arrange_8_queens()
