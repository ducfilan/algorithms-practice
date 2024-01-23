/*
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],

	[1,0,0,0,0,0,1],
	[1,0,1,1,1,0,1],
	[1,0,1,0,1,0,1],
	[1,0,1,1,1,0,1],
	[1,0,0,0,0,0,1],
	[1,1,1,1,1,1,1]]

Output: 2

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
*/
func closedIsland(grid [][]int) int {
	if len(grid) <= 1 {
		return 0
	}

	m, n := len(grid), len(grid[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	islandCount := 0

	var bfs func(i, j int)
	bfs = func(i, j int) {
		queue := make([][]int, 0)
		queue = append(queue, []int{i, j})
		reachBorder := false
		for len(queue) > 0 {
			cell := queue[0]
			queue = queue[1:]
			visited[cell[0]][cell[1]] = true
			if isReachBorder(m, n, cell[0], cell[1]) {
				reachBorder = true
			}
			neighbors := getNeighbors(cell[0], cell[1])

			for _, neighbor := range neighbors {
				if isLand(grid, neighbor[0], neighbor[1]) && !visited[neighbor[0]][neighbor[1]] {
					queue = append(queue, []int{neighbor[0], neighbor[1]})
				}
			}
		}

		if !reachBorder {
			islandCount++
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if isLand(grid, i, j) && !visited[i][j] {
				bfs(i, j)
			}
		}
	}

	return islandCount
}

func getNeighbors(i, j int) [][]int {
	return [][]int{{i - 1, j}, {i, j - 1}, {i + 1, j}, {i, j + 1}}
}

func isLand(grid [][]int, i, j int) bool {
	if isOutOfRange(len(grid), len(grid[0]), i, j) {
		return false
	}

	return grid[i][j] == 0
}

func isReachBorder(m, n, i, j int) bool {
	return i <= 0 || j <= 0 || i >= m-1 || j >= n-1
}

func isOutOfRange(m, n, i, j int) bool {
	return i < 0 || j < 0 || i > m-1 || j > n-1
}
