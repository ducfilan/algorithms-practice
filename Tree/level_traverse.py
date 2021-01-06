from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        if left:
            self.left = TreeNode(left)
        else:
            self.left = None

        if right:
            self.right = TreeNode(right)
        else:
            self.right = None

    def insert_left(self, val):
        self.left = TreeNode(val)

    def insert_right(self, val):
        self.right = TreeNode(val)

def level_traverse(root):
    level_nodes = deque()
    level_nodes.append(root)
    
    while level_nodes:
        node = level_nodes.popleft()
        print(node.val)
        
        if node.left:
            level_nodes.append(node.left)
        
        if node.right:
            level_nodes.append(node.right)

root = TreeNode(1, 2, 3)
left = root.left
left.insert_left(5)
left.insert_right(6)

right = root.right
right.insert_left(7)
right.insert_right(8)

level_traverse(root)