/*
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
*/

import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: the given BST
 * @param target: the given target
 * @return: the value in the BST that is closest to the target
 */
func ClosestValue(root *TreeNode, target float64) int {
    closestNum := root.Val
    var search func(node *TreeNode)
    search = func(node *TreeNode) {
        if node == nil {
            return
        }

        closestNum = findCloser(closestNum, node.Val, target)

        if target < float64(node.Val) {
            search(node.Left)
        } else {
            search(node.Right)
        }
    }

    search(root)

    return closestNum
}

func findCloser(num1, num2 int, target float64) int {
    if math.Abs(float64(num1) - target) > math.Abs(float64(num2) - target) {
        return num2
    }

    return num1
}

