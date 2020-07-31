# Given a square matrix a of order n, its rows and columns are numbered from 0 to n-1.
#
# Your task is to find a path starting from the top left corner cell (0, 0) to the bottom right corner cell
# (n - 1, n - 1) with the following rules: at each turn, you are allowed to move to the right or move down.
# It means if you are at the cell (x, y), you are able to move to the cell (x + 1, y) or (x, y + 1).
# The cost of the path is the sum of values of all the cells which create the path.
#
# Calculate the sum of all the cost of all the possible paths starting from the cell (0, 0) to the cell (n - 1, n - 1).
# Output the answer modulo 1000000007 (109 + 7)
#
# Example:
#
# For n = 2, a = [[3, 4], [5, 1]], the output should be sumAllPath2D(n, a) = 17
# Explanation: There are two paths from (0, 0) to (1, 1)
# Path 1: (0, 0) -> (0, 1) -> (1, 1)
# The cost of this path is: 3 + 4 + 1 = 8
# Path 2: (0, 0) -> (1, 0) -> (1, 1)
# The cost of this path is: 3 + 5 + 1 = 9
# The total cost is: 8 + 9 = 17
#
# For n = 3, a = [[1, 2, 3][4, 5, 6][7, 8, 9]], the output should be sumAllPath2D(n, a) = 150
# Explanation: There are 6 paths from (0, 0) to (2, 2)
# Path 1: (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2)
# The cost of this path is 21
# Path 2: (0, 0) -> (0, 1) -> (1, 1) -> (1, 2) -> (2, 2)
# The cost of this path is 23
# Path 3: (0, 0) -> (0, 1) -> (1, 1) -> (2, 1) -> (2, 2)
# The cost of this path is 25
# Path 4: (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> (2, 2)
# The cost of this path is 25
# Path 5: (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2)
# The cost of this path is 27
# Path 6: (0, 0) -> (1, 0) -> (2, 0) -> (2, 1) -> (2, 2)
# The cost of this path is 29
# The total cost is: 21 + 23 + 25 + 25 + 27 + 29 = 150.

def sum_all_path2D(n, a):
    if not a:
        return 0

    if not a[0]:
        return 0

    dp = [[0 for i in range(n)] for j in range(n)]
    paths_count = [[0 for i in range(n)] for j in range(n)]

    dp[0][0] = a[0][0]

    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + a[0][i]
        paths_count[0][i] += 1

    for j in range(1, n):
        dp[j][0] = dp[j - 1][0] + a[j][0]
        paths_count[j][0] += 1

    for i in range(1, n):
        for j in range(1, n):
            paths_count[i][j] += paths_count[i][j - 1] + paths_count[i - 1][j]
            dp[i][j] += a[i][j] * paths_count[i][j] + dp[i][j - 1] + dp[i - 1][j]

    return dp[n - 1][n - 1] % 1000000007


print(sum_all_path2D(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 150)

print(sum_all_path2D(20, [[38, 3, 36, 16, 22, 78, 7, 25, 45, 90, 14, 17, 60, 50, 24, 33, 64, 87, 44, 37],
                          [68, 21, 28, 76, 26, 95, 49, 36, 65, 36, 3, 37, 83, 29, 67, 61, 22, 49, 62, 68],
                          [5, 26, 29, 2, 57, 28, 99, 3, 97, 82, 53, 91, 80, 13, 72, 66, 34, 25, 68, 34],
                          [83, 54, 4, 78, 93, 43, 60, 13, 80, 21, 99, 13, 70, 80, 4, 83, 79, 68, 43, 36],
                          [67, 18, 99, 44, 21, 90, 50, 60, 45, 32, 8, 30, 15, 30, 13, 93, 28, 98, 56, 67],
                          [86, 74, 38, 11, 72, 48, 90, 44, 96, 9, 42, 5, 96, 44, 61, 65, 63, 90, 60, 6],
                          [22, 51, 6, 18, 4, 70, 76, 53, 18, 11, 14, 55, 16, 22, 64, 57, 63, 92, 61, 3],
                          [20, 96, 71, 6, 66, 64, 17, 91, 72, 26, 67, 40, 40, 25, 55, 45, 73, 2, 89, 25],
                          [13, 28, 65, 94, 8, 16, 87, 24, 94, 1, 2, 58, 44, 45, 52, 45, 39, 50, 7, 70],
                          [96, 58, 54, 1, 91, 24, 44, 4, 65, 60, 12, 89, 63, 14, 70, 41, 3, 30, 59, 52],
                          [36, 80, 84, 9, 28, 81, 13, 20, 48, 98, 75, 56, 90, 39, 66, 90, 96, 6, 34, 56],
                          [60, 17, 88, 85, 84, 8, 24, 45, 47, 48, 98, 36, 42, 86, 64, 76, 99, 28, 48, 94],
                          [67, 93, 10, 2, 39, 85, 100, 86, 33, 43, 29, 23, 72, 25, 49, 27, 68, 55, 94, 99],
                          [76, 60, 8, 30, 86, 81, 20, 43, 13, 90, 95, 50, 83, 85, 45, 52, 58, 19, 67, 92],
                          [77, 73, 82, 43, 58, 4, 12, 62, 3, 23, 10, 77, 69, 78, 9, 75, 14, 1, 94, 86],
                          [44, 73, 59, 74, 44, 18, 68, 44, 50, 84, 9, 7, 21, 91, 56, 89, 89, 24, 68, 8],
                          [32, 81, 88, 19, 66, 46, 84, 53, 16, 37, 76, 7, 95, 44, 80, 6, 23, 87, 82, 57],
                          [35, 14, 61, 18, 6, 58, 10, 81, 54, 2, 62, 43, 85, 61, 15, 14, 31, 67, 79, 52],
                          [28, 82, 22, 64, 58, 47, 64, 41, 3, 57, 9, 21, 75, 26, 62, 21, 22, 41, 82, 40],
                          [8, 79, 54, 13, 32, 34, 66, 88, 52, 65, 68, 43, 75, 12, 58, 41, 71, 86, 49,
                           31]]) == 502683357)
