def to_zombies(matrix, i, j):
    humans = []

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for neighbor in neighbors:
        neighbor_i = i + neighbor[0]
        neighbor_j = j + neighbor[1]

        if neighbor_i < 0 or neighbor_j < 0 or neighbor_i >= len(matrix) or neighbor_j >= len(matrix[0]):
            continue

        if matrix[neighbor_i][neighbor_j] == 0:
            humans.append((neighbor_i, neighbor_j))
            matrix[neighbor_i][neighbor_j] = 1

    return humans


def min_hours(matrix):
    # TODO: Edge cases

    row = len(matrix)
    col = len(matrix[0])

    hours_count = 0

    zombie_cells = [(i, j) for i in range(row) for j in range(col) if matrix[i][j] == 1]

    while True:
        humans_affected = []

        for i, j in zombie_cells:
            if matrix[i][j] == 1:
                humans_affected += to_zombies(matrix, i, j)
        if not humans_affected:
            break
        zombie_cells = humans_affected
        hours_count += 1

    return hours_count


print(min_hours([[0, 1, 1, 0, 1],
                 [0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 0]]
                ))
