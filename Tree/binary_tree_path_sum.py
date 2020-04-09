# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf
# such that the sum of all the node values of that path equals ‘S’.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class Result:
    def __init__(self, is_path_exist, path):
        self.is_path_exist = is_path_exist
        self.path = path


def dfs(node, target_sum, sum, path, all_paths):
    path.append(node)  # List of nodes that sums equals to the target sum.

    sum += node.value

    if node.is_leaf() and sum == target_sum:
        all_paths.append(list(path))
    else:
        if node.left:
            dfs(node.left, target_sum, sum, path, all_paths)

        if node.right:
            dfs(node.right, target_sum, sum, path, all_paths)

    del path[-1]


def find_path_sum(root, target_sum):
    all_paths = []
    dfs(root, target_sum, 0, [], all_paths)
    return all_paths


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(6))

print([[node.value for node in path] for path in find_path_sum(root, 10)])
