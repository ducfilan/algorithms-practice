/*
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
*/

func minReorder(n int, connections [][]int) int {
    graph := make([][]int, n)
    for _, edge := range connections {
        graph[edge[0]] = append(graph[edge[0]], edge[1])
        graph[edge[1]] = append(graph[edge[1]], edge[0])
    }

    level := make([]int, n)
    visited := make([]bool, n)
    traverseQueue := []int{0}
    visited[0] = true

    for len(traverseQueue) > 0 {
        currentCity := traverseQueue[0]
        traverseQueue = traverseQueue[1:]

        for _, neighbor := range graph[currentCity] {
            if !visited[neighbor] {
                level[neighbor] = level[currentCity] + 1
                visited[neighbor] = true
                traverseQueue = append(traverseQueue, neighbor)
            }
        }
    }

    changes := 0
    for _, connection := range connections {
        fromCity := connection[0]
        toCity := connection[1]
        if level[fromCity] < level[toCity] {
            changes++
        }
    }

    return changes
}
