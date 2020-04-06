# Level: HARD
#
# Sample Input: 3141592653589793238462643383279
# Words: ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']
# Sample Output: 3 (314 15926535897 9323 8462643383279)


class TrieNode:
    def __init__(self, value, is_end=False):
        self.value = value
        self.children = {}
        self.is_end = is_end

    def add_child(self, child_value, is_end=False):
        self.children[child_value] = TrieNode(child_value, is_end)

        return self.children[child_value]


class Solution:
    def __init__(self, string, words):
        self.string = string
        self.words = words
        self.root = TrieNode(None)

    def build_trie(self):
        current_node = self.root

        for word in self.words:
            for c in word:
                if c in current_node.children:
                    current_node = current_node.children[c]
                else:
                    current_node = current_node.add_child(c)

            current_node.is_end = True
            current_node = self.root

    def find_min_spaces(self, sub_string=None, memo={}):
        if sub_string is None:
            sub_string = self.string

        if sub_string in memo:
            return memo[sub_string]

        space_count = 0

        current_node = self.root

        for i in range(len(sub_string)):
            num = sub_string[i]

            if num not in current_node.children:
                space_count = -1
                break
            else:
                if current_node.children[num].is_end:
                    if i < len(sub_string) - 1:
                        space_count += 1

                    part_space_count = self.find_min_spaces(
                        sub_string[i+1:], memo)
                    if part_space_count == -1:
                        space_count -= 1
                        current_node = current_node.children[num]
                        continue

                    space_count += part_space_count
                    break
                elif i == len(sub_string) - 1:
                    return -1

                current_node = current_node.children[num]

        memo[sub_string] = space_count
        return space_count


s = Solution('3141592653589793238462643383279',
             ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793'])

s.build_trie()

# print(s.find_min_spaces())

s = Solution('aaaaaaa',
             ['aaaa', 'aa'])

s.build_trie()

#print(s.find_min_spaces())

s = Solution('ab',
             ['b', 'a'])

s.build_trie()

print(s.find_min_spaces())
