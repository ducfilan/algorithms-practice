'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_to_linked_list(root):
    if not root:
        return

    nodes = [root]
    prev_node = None

    while len(nodes) > 0:
        print(len(nodes))
        node = nodes.pop()

        if prev_node:
            prev_node.left = None
            prev_node.right = node

        prev_node = node

        if node.right:
            nodes.append(node.right)

        if node.left:
            nodes.append(node.left)


def level_traverse(root):
    level_nodes = deque()
    level_nodes.append(root)
    print(f'root: {root.val}')

    while level_nodes:
        node = level_nodes.popleft()

        if node.left:
            print(f'left: {node.left.val}')
            level_nodes.append(node.left)

        if node.right:
            print(f'right: {node.right.val}')
            level_nodes.append(node.right)


root = TreeNode(1, TreeNode(2), TreeNode(3))
left = root.left
left.left = TreeNode(5)
left.right = TreeNode(6)

right = root.right
right.left = TreeNode(7)
right.right = TreeNode(8)
right.right.left = TreeNode(9)
right.right.right = TreeNode(10)
right.left.left = TreeNode(11)
right.left.right = TreeNode(12)

level_traverse(root)
binary_to_linked_list(root)
level_traverse(root)
