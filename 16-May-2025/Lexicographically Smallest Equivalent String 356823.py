# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
            
        for s1,s2 in zip(s1,s2):
            union(ord(s1) - ord('a'), ord(s2) - ord('a'))

        ans = []
        for c in baseStr:
            ans.append(chr(find(ord(c) - ord('a')) + ord('a')))
        return "".join(ans)
