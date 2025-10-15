# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index,root):
            cur = root
            for i in range(index,len(word)):
                char = word[i]
                if char == '.':
                    for child in cur.children.values():
                        if dfs(i + 1,child):
                            return True
                    return False
                    
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.is_end
        return dfs(0,self.root)
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)