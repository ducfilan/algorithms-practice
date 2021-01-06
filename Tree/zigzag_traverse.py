'''
Given a binary tree, return the zigzag level order traversal （from left to right, then right to left for the next level and alternate between）
Use a comma as a separator between each node in the same level, use '#' as a separator after a level.
 
Given binary tree [1, 2, 3, null null, 6, 7],
    1
   / \
  2   3
    /  \
   6   7
 
 
 Expect output:
1#3,2#6,7#


JavaScript:
function TreeNode(val) {
      this.val = val;
      this.left = this.right = null;
}

Input TreeNode
root = new TreeNode(1)
root.left = new  TreeNode(2)
root.right = new  TreeNode(3)
root.right.left = new TreeNode(6)
root.right.left = new TreeNode(7)
 
Expect output:
1#3,2#6,7#
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def zigzag_traverse(root):
    if not root:
        return

    current_level_nodes = []
    next_level_nodes = []

    zigzag_flag = True

    output_vals_current_level = []

    current_level_nodes.append(root)

    while len(current_level_nodes) > 0:
        node = current_level_nodes.pop()

        output_vals_current_level.append(node.val)

        if zigzag_flag:
            if node.left:
                next_level_nodes.append(node.left)

            if node.right:
                next_level_nodes.append(node.right)
        else:
            if node.right:
                next_level_nodes.append(node.right)

            if node.left:
                next_level_nodes.append(node.left)

        if len(current_level_nodes) == 0:
            print(','.join(map(str, output_vals_current_level)), end='#')
            output_vals_current_level = []

            zigzag_flag = not zigzag_flag
            current_level_nodes = next_level_nodes
            next_level_nodes = []


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

zigzag_traverse(root)
