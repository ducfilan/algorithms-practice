def cell_compete(cells, days):
    current_day_cells = [0, *cells, 0]
    next_day_active_cells = current_day_cells[:]

    for day in range(days):
        for i in range(1, len(current_day_cells) - 1):
            if current_day_cells[i - 1] == current_day_cells[i + 1]:
                next_day_active_cells[i] = 0
            else:
                next_day_active_cells[i] = 1
        current_day_cells = next_day_active_cells[:]

    return current_day_cells[1:-1]


if __name__ == '__main__':
    print(cell_compete([1, 1, 1, 0, 1, 1, 1, 1], 2))
