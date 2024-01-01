/*
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
*/

var adjCellsDiff [][]int = [][]int{
    {-1, 0},
    {1, 0},
    {0, -1},
    {0, 1},
}

func orangesRotting(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    rottenCells := [][]int{}
    freshCount := 0

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            isFresh := grid[i][j] == 1
            isRotten := grid[i][j] == 2
            if isRotten {
                rottenCells = append(rottenCells, []int{i, j})
            }else if isFresh {
                freshCount++
            }
        }
    }

    if freshCount == 0 {
        return 0
    }

    minutes := 0

    for len(rottenCells) > 0 {
        currentRottenCellsCount := len(rottenCells)
        for i := 0; i < currentRottenCellsCount; i++ {
            cell := rottenCells[0]
            rottenCells = rottenCells[1:]

            for _, adjCellDiff := range adjCellsDiff {
                adjCellI := cell[0] + adjCellDiff[0]
                adjCellJ := cell[1] + adjCellDiff[1]

                isOutOfRange := adjCellI < 0 || adjCellJ < 0 || adjCellI > m - 1 || adjCellJ > n - 1
                if isOutOfRange {
                    continue
                }

                isFresh := grid[adjCellI][adjCellJ] == 1
                if isFresh {
                    grid[adjCellI][adjCellJ] = 2
                    rottenCells = append(rottenCells, []int{adjCellI, adjCellJ})
                    freshCount--
                }
            }
        }

        minutes++
    }

    if freshCount > 0 {
        return -1
    }

    return minutes - 1
}
