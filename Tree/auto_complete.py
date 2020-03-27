class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_end = False

    def add_child(self, child_value):
        child_node = TrieNode(child_value)
        self.children[child_value] = child_node

        return child_node


def find_words(node, prefix):
    words = []

    if node.is_end:
        words += [prefix]

    for child in node.children.values():
        words += find_words(child, prefix + child.value)

    return words


def auto_complete(prefix, dictionary):
    current_node = build_trie(dictionary)

    for c in prefix:
        if c not in current_node.children:
            return []
        current_node = current_node.children[c]

    return find_words(current_node, prefix)


def build_trie(dictionary):
    root = TrieNode(None)
    current_node = root

    for word in dictionary:
        for c in word:
            if c in current_node.children:
                current_node = current_node.children[c]
            else:
                current_node = current_node.add_child(c)

        current_node.is_end = True

        current_node = root

    return root


print(auto_complete('ab', ['ab', 'abc', 'abd', 'abcde',
                           'bcd', 'bce', 'bcdef', 'cde', 'def']))
