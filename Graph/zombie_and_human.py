def to_zombies(matrix, i, j):
    human_count = 0

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for neighbor in neighbors:
        neighbor_i = i + neighbor[0]
        neighbor_j = j + neighbor[1]

        if neighbor_i < 0 or neighbor_j < 0 or neighbor_i >= len(matrix) or neighbor_j >= len(matrix[0]):
            continue

        if matrix[neighbor_i][neighbor_j] == 0:
            human_count += 1
            matrix[neighbor_i][neighbor_j] = 1

    return human_count


def min_hours(matrix):
    # TODO: Edge cases

    row = len(matrix)
    col = len(matrix[0])

    hours_count = 0

    while True:
        human_count = 0
        zombie_cells = [(i, j) for i in range(row) for j in range(col) if matrix[i][j] == 1]

        for i, j in zombie_cells:
            if matrix[i][j] == 1:
                human_count += to_zombies(matrix, i, j)
        if human_count == 0:
            break

        hours_count += 1

    return hours_count


print(min_hours([[0, 1, 1, 0, 1],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0]]
                ))
