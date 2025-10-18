# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        change = val - self.values.get(key, 0)
        self.values[key] = val

        node = self.root
        node.value += change

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.value += change

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.value


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)