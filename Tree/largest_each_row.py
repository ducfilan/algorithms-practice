'''
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Input: root = [1,2,3]
Output: [1,3]
Input: root = [1]
Output: [1]
Input: root = [1,null,2]
Output: [1,2]
Input: root = []
Output: []
'''

from heapq import heappush, heappop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        if not root:
            return []

        current_level_nodes = []
        current_level_nodes_vals_heap = []
        next_level_nodes = []

        current_level_nodes.append(root)
        output = []

        while len(current_level_nodes) > 0:
            node = current_level_nodes.pop()
            heappush(current_level_nodes_vals_heap, -node.val)

            if node.left:
                next_level_nodes.append(node.left)

            if node.right:
                next_level_nodes.append(node.right)

            if len(current_level_nodes) == 0:
                current_level_nodes = next_level_nodes
                next_level_nodes = []

                output.append(-heappop(current_level_nodes_vals_heap))
                current_level_nodes_vals_heap = []

        return output

root = TreeNode(1, TreeNode(2), TreeNode(3))
left = root.left
left.left = TreeNode(5)
left.right = TreeNode(6)

right = root.right
right.left = TreeNode(7)
right.right = TreeNode(8)

sol = Solution()
print(sol.largestValues(root))

root = TreeNode(1, TreeNode(3), TreeNode(2))
left = root.left
left.left = TreeNode(5)
left.right = TreeNode(3)

right = root.right
right.right = TreeNode(9)

sol = Solution()
print(sol.largestValues(root))

root = TreeNode(1, TreeNode(2), TreeNode(3))

sol = Solution()
print(sol.largestValues(root))

root = TreeNode(1)

sol = Solution()
print(sol.largestValues(root))

root = TreeNode(1, None, TreeNode(2))

sol = Solution()
print(sol.largestValues(root))

root = None

sol = Solution()
print(sol.largestValues(root))

root = TreeNode(1, TreeNode(2), TreeNode(-3))

sol = Solution()
print(sol.largestValues(root))