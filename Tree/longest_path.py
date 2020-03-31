class TreeNode:
    def __init__(self, value, parrent_node=None):
        self.value = value
        self.parrent = parrent_node
        self.left = None
        self.right = None

    def insert_left(self, left_node_value):
        self.left = TreeNode(left_node_value, self)
        return self.left

    def insert_right(self, right_node_value):
        self.right = TreeNode(right_node_value, self)
        return self.right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_parent(self):
        return self.parent


class Solution:
    def __init__(self, root):
        self.root = root
        self.longest_path = 0

    def find_longest_path(self):
        self._traverse_tree_nodes(self.root)

        return self.longest_path

    def _traverse_tree_nodes(self, node, current_length=0):
        if current_length > self.longest_path:
            self.longest_path = current_length

        if node.get_left_child():
            self._traverse_tree_nodes(node.get_left_child(), current_length+1)

        if node.get_right_child():
            self._traverse_tree_nodes(node.get_right_child(), current_length+1)


# Init tree
root = TreeNode(1)
root.insert_left(1)
root.insert_right(1)
root.get_right_child().insert_left(1)
root.get_right_child().insert_right(1)
root.get_right_child().get_right_child().insert_left(1)
root.get_right_child().get_right_child().insert_right(1)

# Process
s = Solution(root)
print(s.find_longest_path())
