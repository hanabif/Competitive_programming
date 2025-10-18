# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
    
    def longest_word(self) -> str:
        self.best = ""
        def dfs(node: TrieNode, path: list):
            if node is not self.root and not node.is_end:
                return
            word = "".join(path)
            if len(word) > len(self.best) or (len(word) == len(self.best) and word < self.best):
                self.best = word
            for ch in sorted(node.children.keys()):
                dfs(node.children[ch], path + [ch])

        dfs(self.root, [])
        return self.best

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.longest_word()
        

        