# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count = 0

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
            curr.count += 1

    def score(self,word):
        cur = self.root
        score = 0
        for w in word:
            index = ord(w) - ord('a')
            cur = cur.children[index]
            score += cur.count
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        trie = Trie()

        for w in words:
            trie.insert(w)
        
        for w in words:
            res.append(trie.score(w))
        
        return res