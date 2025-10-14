# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
        
    def shortest(self, word: str) -> str:
        curr = self.root
        prefix = []
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return word  
            curr = curr.children[index]
            prefix.append(c)
            if curr.is_end:
                return "".join(prefix)  
        return word  

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        words = sentence.split()
        
        for s in dictionary:
            trie.insert(s)
        
        result = []
        for word in words:
            result.append(trie.shortest(word))
        return ' '.join(result)
        
