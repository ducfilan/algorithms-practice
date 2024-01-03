package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	var currentLevelNodes []*TreeNode
	var nextLevelNodes []*TreeNode
	currentLevelNodes = append(currentLevelNodes, root)
	var res [][]int
	ltr := true
	var node *TreeNode

	for len(currentLevelNodes) > 0 {
		size := len(currentLevelNodes)
		levelNodes := make([]int, size)

		for i := 0; i < size; i++ {
			node = currentLevelNodes[size-i-1]
			currentLevelNodes = currentLevelNodes[:size-i-1]

			if ltr {
				if node.Left != nil {
					nextLevelNodes = append(nextLevelNodes, node.Left)
				}

				if node.Right != nil {
					nextLevelNodes = append(nextLevelNodes, node.Right)
				}
			} else {
				if node.Right != nil {
					nextLevelNodes = append(nextLevelNodes, node.Right)
				}

				if node.Left != nil {
					nextLevelNodes = append(nextLevelNodes, node.Left)
				}
			}

			levelNodes[i] = node.Val
		}

		ltr = !ltr
		res = append(res, levelNodes)
		currentLevelNodes = nextLevelNodes
		nextLevelNodes = []*TreeNode{}
	}

	return res
}

func main() {
	root := &TreeNode{
		Val: 0,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 5,
				},
			},
		},
		Right: &TreeNode{
			Val: 4,
			Left: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 1,
				},
				Right: &TreeNode{
					Val: 6,
				},
			},
			Right: &TreeNode{
				Val: -1,
				Right: &TreeNode{
					Val: 8,
				},
			},
		},
	}

	res := zigzagLevelOrder(root)
	for _, v := range res {
		for _, vv := range v {
			fmt.Printf("%d ", vv)
		}
		fmt.Println()
	}
}

//       0
//      / \
//     2   4
//    /   / \
//   1   3  -1
//  /   / \   \
// 5   1   6   8
