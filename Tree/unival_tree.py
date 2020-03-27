# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# 
# Given the root to a binary tree, count the number of unival subtrees.
# 
# For example, the following tree has 5 unival subtrees:
# 
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


import os.path
import sys

sys.path.extend(
    [os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))])

from Tree.DS.binary_tree import TreeNode


def unival_tree(root):
    count = 0
    is_unival = True

    if root.get_left_child() is None and root.get_right_child() is None:
        count += 1

    if root.get_left_child() is not None:
        left_child = root.get_left_child()
        count += unival_tree(left_child)
        if left_child.get_value() != root.get_value():
          is_unival = False

    if root.get_right_child() is not None:
        right_child = root.get_right_child()
        count += unival_tree(right_child)
        if right_child.get_value() != root.get_value():
          is_unival = False

    if is_unival and root.get_left_child() is not None and root.get_right_child() is not None:
      count += 1

    return count


tree = TreeNode(0)
tree.insert_left(1)
tree.insert_right(0)
tree.get_right_child().insert_right(0)
tree.get_right_child().insert_left(1)
tree.get_right_child().get_left_child().insert_left(1)
tree.get_right_child().get_left_child().insert_right(1)

print(unival_tree(tree))
