class TreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = None
        self.right = None

    def insert_left(self, left_node_value):
        self.left = TreeNode(left_node_value)

    def insert_right(self, right_node_value):
        self.right = TreeNode(right_node_value)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class Solution:
    def count_nodes(self, from_node):
        if not from_node:
            return 0

        nodes_count = 1

        if from_node.get_left():
            nodes_count += self.count_nodes(from_node.get_left())
        
        if from_node.get_right():
            nodes_count += self.count_nodes(from_node.get_right())

        return nodes_count

root = TreeNode(1)
root.insert_left(2)
root.insert_right(3)
root.get_left().insert_left(4)
root.get_left().insert_right(5)

s = Solution()
print(s.count_nodes(root))
