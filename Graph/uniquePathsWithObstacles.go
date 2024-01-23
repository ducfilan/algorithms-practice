/*
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
*/

func uniquePathsWithObstacles2(obstacleGrid [][]int) int {
    m, n := len(obstacleGrid), len(obstacleGrid[0])
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
    }

    // If the start cell has an obstacle, then return 0
    if obstacleGrid[0][0] == 1 {
        return 0
    } else {
        dp[0][0] = 1
    }

    // Fill the first row and column
    for i := 1; i < m; i++ {
        if obstacleGrid[i][0] == 0 && dp[i-1][0] == 1 {
            dp[i][0] = 1
        }
    }
    for j := 1; j < n; j++ {
        if obstacleGrid[0][j] == 0 && dp[0][j-1] == 1 {
            dp[0][j] = 1
        }
    }

    // Fill the rest of the table
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if obstacleGrid[i][j] == 0 {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
        }
    }

    // Return the value in the bottom-right cell
    return dp[m-1][n-1]
}



func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if len(obstacleGrid) == 0 || isObstacle(obstacleGrid, 0, 0) {
		return 0
	}

	m, n := len(obstacleGrid), len(obstacleGrid[0])
	result := 0
	var dfs func(i, j int)
	dfs = func(i, j int) {
		if !isObstacle(obstacleGrid, i, j) && isReachTarget(m, n, i, j) {
			result++
		}

		if !isOutside(m, n, i+1, j) && !isObstacle(obstacleGrid, i+1, j) {
			dfs(i+1, j)
		}

		if !isOutside(m, n, i, j+1) && !isObstacle(obstacleGrid, i, j+1) {
			dfs(i, j+1)
		}
	}

	dfs(0, 0)

	return result
}

func isReachTarget(m, n, i, j int) bool {
	return i == m-1 && j == n-1
}

func isObstacle(obstacleGrid [][]int, i, j int) bool {
	return obstacleGrid[i][j] == 1
}

func isOutside(m, n, i, j int) bool {
	return i >= m || j >= n
}
