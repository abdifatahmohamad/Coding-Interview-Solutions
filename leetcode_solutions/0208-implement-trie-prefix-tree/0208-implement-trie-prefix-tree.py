class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.get_node(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self.get_node(prefix) is not None

    def get_node(self, word: str) -> 'TrieNode':
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


