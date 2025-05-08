# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = {i: i for i in range(n + 1)}
        size = [1 for _ in range(n + 1)]

        def find(x): 
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(i, j):
            pi = find(i)
            pj = find(j)

            if pi != pj:
                if size[pi] > size[pj]:
                    parent[pj] = parent[pi]
                    size[pi] += size[pj]
                    size[pj] = 1
                else:
                    parent[pi] = parent[pj]
                    size[pj] += size[pi]
                    size[pi] = 1
        for i in range(n):
            x1 , y1 = stones[i]
            for j in range(i + 1, n):
                x2 , y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    union(i,j)
                
        ans = 0
        for i in range(len(size)):
            ans += size[i] - 1
        return ans
