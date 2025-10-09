# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        
        if curr.is_end == True:
            return True
        else:
            return False
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)