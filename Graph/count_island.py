def visit_neighbors(matrix, visited, i, j):
    visited[i][j] = True
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for neighbor in neighbors:
        neighbor_i = i + neighbor[0]
        neighbor_j = j + neighbor[1]

        if neighbor_i < 0 or neighbor_j < 0 or neighbor_i >= len(matrix) or neighbor_j >= len(matrix[0]):
            continue

        if not visited[neighbor_i][neighbor_j] and matrix[neighbor_i][neighbor_j] == 1:
            visited[neighbor_i][neighbor_j] = True
            visit_neighbors(matrix, visited, neighbor_i, neighbor_j)


def count_island(matrix):
    row = len(matrix)
    col = len(matrix[0])

    visited = [[False for i in range(col)] for j in range(row)]

    island_count = 0

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and not visited[i][j]:
                visit_neighbors(matrix, visited, i, j)
                island_count += 1

    return island_count


print(count_island([
    [1, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1]
]))
