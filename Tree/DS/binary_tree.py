class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node_value):
        new_node = TreeNode(new_node_value)

        if self.left_child:
            new_node.left_child = self.left_child
            self.left_child = new_node
        else:
            self.left_child = new_node

    def insert_right(self, new_node_value):
        new_node = TreeNode(new_node_value)

        if self.right_child:
            new_node.right_child = self.right_child
            self.right_child = new_node
        else:
            self.right_child = new_node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_value(self):
        return self.value

    def set_root_value(self, new_value):
        self.key = new_value

    def pre_order_traverse(self, tree):
        if tree:
            print(tree.get_value())
            self.in_order_traverse(tree.get_left_child())
            self.in_order_traverse(tree.get_right_child())

    def in_order_traverse(self, tree):
        if tree:
            self.in_order_traverse(tree.get_left_child())
            print(tree.get_value())
            self.in_order_traverse(tree.get_right_child())

    def post_order_traverse(self, tree):
        if tree:
            self.in_order_traverse(tree.get_left_child())
            self.in_order_traverse(tree.get_right_child())
            print(tree.get_value())
