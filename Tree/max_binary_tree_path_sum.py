class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value

        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def find_max_binary_tree_path_sum(node):
    if node is None:
        return 0

    left_sum = find_max_binary_tree_path_sum(node.left)
    right_sum = find_max_binary_tree_path_sum(node.right)

    return node.value + max(left_sum, right_sum)


root = Node(1)
root.left = Node(2, Node(4), Node(5))
root.right = Node(3, Node(6), Node(7))

print(find_max_binary_tree_path_sum(root))
