# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.ind = []

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, index: int) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.ind.append(index)
   
    def startsWith(self, prefix: str) -> List[int]:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]
        return curr.ind

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = Trie()
        self.suffix = Trie()

        for i, w in enumerate(words):
            self.prefix.insert(w, i)
            self.suffix.insert(w[::-1], i)

    def f(self, pref: str, suff: str) -> int:
        p = self.prefix.startsWith(pref)
        s = self.suffix.startsWith(suff[::-1])

        i = len(p) - 1
        j = len(s) - 1
        while i >= 0 and j >= 0:
            if p[i] == s[j]:
                return p[i]
            elif p[i] > s[j]:
                i -= 1
            else:
                j -= 1
        
        return -1



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)