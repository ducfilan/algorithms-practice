result = []


def arrange_8_queens(queen_no=1):
    for i in range(1, 9):
        is_next = False
        for r in result:
            if i == r[0] or r[0] + r[1] == i + queen_no or r[0] - r[1] == i - queen_no:
                is_next = True
                break

        if is_next:
            if i == 8:
                element_to_del = result[-1]
                if element_to_del[0] == 8:
                    del result[-2:]
                else:
                    del result[-1]

            continue

        result.append((i, queen_no))

        if len(result) == 8:
            print(result)
            element_to_del = result[-1]
            if element_to_del[0] == 8:
                del result[-2:]
            else:
                del result[-1]
        elif queen_no < 8:
            arrange_8_queens(queen_no + 1)


if __name__ == '__main__':
    arrange_8_queens()
